#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  moneydero.py
#
#  Copyright 2014 Felipe Hommen <felibank@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#


import sys
import datetime
from PyQt4 import QtCore
from PyQt4.QtGui import QApplication, QMainWindow, QDialog, QFrame
from moneydero_ui import Ui_MainWindow
from apuntes_ui import Ui_Dialog
from registro_ui import Ui_Frame
import gestion


class Main_ui(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main_ui, self).__init__()
        self.setupUi(self)
        
        self.filtro = {}
        self.filtro['fecha_desde'] = datetime.date.today()
        self.filtro['fecha_hasta'] = datetime.date.today()
        self.filtro['cuentas'] = 'Todas'
        self.filtro['signo'] = None
        self.filtro['ig'] = 'Ingresos y gastos'
        self.filtro['orden'] = 'reciente'
        
        self.pushButton_apunte.clicked.connect(self.nuevo_apunte)
        self.combo_T.activated.connect(self.cambio_T)
        self.combo_signo.activated.connect(self.cambio_signo)
        self.apuntes_dialog = Apuntes_ui()
        self.update_registro()
        
        
    def nuevo_apunte(self):
        self.apuntes_dialog.exec_()
        self.update_registro()
        
    def update_registro(self):
        for i in reversed(range(self.layout_registro.count())):
            self.layout_registro.itemAt(i).widget().close()
        msg = str(self.combo_signo.currentText()) + ' de ' + \
                str(self.combo_T.currentText()).lower() + ' en ' + \
                str(self.combo_cuenta.currentText())
        self.groupBox_4.setTitle(msg)
        apuntes = gestion.lista_apuntes(self.filtro)
        for apunte in apuntes:
            print('Apunte')
            entrada = Registro_ui(apunte)
            self.layout_registro.addWidget(entrada)
            
    def cambio_signo(self):
        texto = str(self.combo_signo.currentText())
        if texto == 'Ingresos y gastos':
            self.filtro['signo'] = None
        elif texto == 'Ingresos':
            self.filtro['signo'] = '+'
        elif texto == 'Gastos':
            self.filtro['signo'] = '-'
        self.update_registro()
        
    def cambio_T(self):
        texto = str(self.combo_T.currentText())
        hoy = datetime.date.today()
        dia_semana = hoy.weekday()
        dia_mes = hoy.day
        if texto == 'Hoy':
            self.filtro['fecha_desde'] = hoy
            self.filtro['fecha_hasta'] = hoy
        elif texto == 'Esta semana':
            self.filtro['fecha_desde'] = hoy - datetime.timedelta(days=dia_semana)
            self.filtro['fecha_hasta'] = hoy + datetime.timedelta(days=6 - dia_semana)
        elif texto == u'Últimos 7 dias':
            self.filtro['fecha_desde'] = hoy - datetime.timedelta(days=6)
            self.filtro['fecha_hasta'] = hoy
        elif texto == 'Este mes':
            self.filtro['fecha_desde'] = hoy - datetime.timedelta(days=dia_mes - 1)
            mes = hoy.month
            year = hoy.year
            if mes == 12:
                mes = 1
                year = year + 1
            else:
                mes = mes + 1
            self.filtro['fecha_hasta'] = datetime.date(year, mes,  1) - datetime.timedelta(days=1)
        elif texto == 'Últimos 30 dias':
            self.filtro['fecha_desde'] = hoy - datetime.timedelta(days=30)
            self.filtro['fecha_hasta'] = hoy
        elif texto == 'Este año':
            self.filtro['fecha_desde'] = datetime.date(year,  1, 1)
            self.filtro['fecha_hasta'] = datetime.date(year,  12,  31)
        elif texto == 'Todo':
            self.filtro['fecha_desde'] = None
            self.flitro['fecha_hasta'] = None
        self.update_registro()
        
class Apuntes_ui(QDialog, Ui_Dialog):
    def __init__(self):
        super(Apuntes_ui, self).__init__()
        self.setupUi(self)
        self.dateEdit_fecha.setDateTime(QtCore.QDateTime.currentDateTime())
        for c in sorted(gestion.categorias):
            self.comboBox_categoria.addItem(c)
        self.comboBox_categoria.addItem('Añadir categoria')
        for s in sorted(gestion.socios):
            self.comboBox_vendedor.addItem(s)
        for c in sorted(gestion.cuentas):
            self.comboBox_cuenta.addItem(c)
        
        self.pushButton_guardar.clicked.connect(self.guardar)
        self.pushButton_cancelar.clicked.connect(self.close)
        self.pushButton_gasto.clicked.connect(self.toggle_gasto)
        self.comboBox_categoria.activated.connect(self.nueva_categoria)
        
    def guardar(self):
        year = self.dateEdit_fecha.date().year()
        month = self.dateEdit_fecha.date().month()
        day = self.dateEdit_fecha.date().day()
        fecha = datetime.date(year,  month,  day)
        apunte = {
            'fecha': fecha.isoformat(), 
            'cantidad': str(self.doubleSpinBox.prefix()) + str(self.doubleSpinBox.cleanText()),
            'concepto': str(self.lineEdit_concepto.text()), 
            'cuenta': str(self.comboBox_cuenta.currentText()), 
            'categoria': str(self.comboBox_categoria.currentText()),
            'socio': str(self.comboBox_vendedor.currentText())
            }
        self.comboBox_vendedor.addItem(self.comboBox_vendedor.currentText())
        gestion.apunta(apunte)
        self.close()
        
    def toggle_gasto(self):
        if str(self.pushButton_gasto.text()) == 'Gasto':
            self.pushButton_gasto.setText('Ingreso')
            self.doubleSpinBox.setPrefix('+')
        else:
            self.pushButton_gasto.setText('Gasto')
            self.doubleSpinBox.setPrefix('-')
            
    def nueva_categoria(self,  i):
        texto = str(self.comboBox_categoria.currentText())
        print(texto)
        if texto == 'Añadir categoria':
            self.comboBox_categoria.setEditable(True)
            self.comboBox_categoria.lineEdit().selectAll()
        else:
            if self.comboBox_categoria.isEditable():
                self.comboBox_categoria.setEditable(False)
                nuevo = str(self.comboBox_categoria.currentText())
                self.comboBox_categoria.setEditable(False)
                lista = [self.comboBox_categoria.itemText(c)
                         for c in range(self.comboBox_categoria.count())]
                lista.remove('Añadir categoria')
                lista.sort()
                self.comboBox_categoria.clear()
                for c in lista:
                    self.comboBox_categoria.addItem(c)
                self.comboBox_categoria.addItem('Añadir categoria')
                self.comboBox_categoria.setCurrentIndex(lista.index(nuevo))
                
        
class Registro_ui(QFrame,  Ui_Frame):
    def __init__(self, apunte):
        super(Registro_ui,  self).__init__()
        self.setupUi(self)
        self.label_categoria.setText(gestion.apuntes[apunte]['categoria'])
        self.label_concepto.setText(gestion.apuntes[apunte]['concepto'])
        self.label_socio.setText(gestion.apuntes[apunte]['socio'])
        fecha = gestion.apuntes[apunte]['fecha'].split('-')
        self.label_fecha.setText('{dia} de {mes} de {year}'.format(
            dia=fecha[2],  mes=datetime.date(1, int(fecha[1]), 1).strftime('%B'),  year=fecha[0]))
        self.label_cantidad.setText(gestion.apuntes[apunte]['cantidad'])
        if str(self.label_cantidad.text())[0] == '-':
            self.label_cantidad.setStyleSheet('color: red')
        self.label_cuenta.setText(gestion.apuntes[apunte]['cuenta'])
        
        #self.label_categoria.clicked.connect(self.resalta)
        
    def resalta(self):
        self.setStyleSheet("QFrame { background-color: Red }")
    

def main():
    app = QApplication(sys.argv)
    ui = Main_ui()
    ui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
 
