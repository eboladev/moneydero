#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  monedero.py
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
from PyQt4.QtGui import QApplication, QMainWindow, QDialog,  QWidget
from moneydero_ui import Ui_MainWindow
from apuntes_ui import Ui_Dialog
from registro_ui import Ui_Form
import gestion


class Main_ui(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main_ui, self).__init__()
        self.setupUi(self)
        
        self.filtro = {}
        self.filtro['fecha_desde'] = datetime.date.today()
        self.filtro['fecha_hasta'] = datetime.date.today()
        self.filtro['cuentas'] = 'Todas'
        self.filtro['ig'] = 'Ingresos y gastos'
        
        self.pushButton_apunte.clicked.connect(self.nuevo_apunte)
        self.apuntes_dialog = Apuntes_ui()
        
        self.update_registro
        
        
    def nuevo_apunte(self):
        self.apuntes_dialog.exec_()
        self.update_registro()
        
    def update_registro(self):
        apuntes = gestion.lista_apuntes(self.filtro)
        for apunte in apuntes:
            print('Apunte')
            entrada = Registro_ui(apunte)
            self.layout_registro.addWidget(entrada)
        
        
class Apuntes_ui(QDialog, Ui_Dialog):
    def __init__(self):
        super(Apuntes_ui, self).__init__()
        self.setupUi(self)
        self.dateEdit_fecha.setDateTime(QtCore.QDateTime.currentDateTime())
        self.pushButton_guardar.clicked.connect(self.guardar)
        
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
        gestion.apunta(apunte)
        self.close()
        
class Registro_ui(QWidget,  Ui_Form):
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
        self.label_cuenta.setText(gestion.apuntes[apunte]['cuenta'])
    

def main():
    app = QApplication(sys.argv)
    ui = Main_ui()
    ui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
 
