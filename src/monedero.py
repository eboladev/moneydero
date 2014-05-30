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
from PyQt4 import QtCore
from PyQt4.QtGui import QApplication, QMainWindow, QDialog
from monedero_ui import Ui_MainWindow
from apuntes_ui import Ui_Dialog
import gestion


class Main_ui(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main_ui, self).__init__()
        self.setupUi(self)
        
        self.pushButton_apunte.clicked.connect(self.nuevo_apunte)
        self.apuntes_dialog = Apuntes_ui()
        
        
    def nuevo_apunte(self):
        self.apuntes_dialog.exec_()
        
        
class Apuntes_ui(QDialog, Ui_Dialog):
    def __init__(self):
        super(Apuntes_ui, self).__init__()
        self.setupUi(self)
        
        self.pushButton_guardar.clicked.connect(self.guardar)
        
    def guardar(self):
        apunte = {
            'Fecha': '/'.join([str(self.dateEdit_fecha.date().year()), str(self.dateEdit_fecha.date().month()), str(self.dateEdit_fecha.date().day())]), 
            'Cantidad': self.doubleSpinBox.value(),
            'Concepto': str(self.lineEdit_concepto.text()), 
            'Cuenta': str(self.comboBox_cuenta.currentText()), 
            'Categoria': str(self.comboBox_categoria.currentText()),
            'Socio': str(self.comboBox_vendedor.currentText())
            }
        gestion.apunta(apunte)
        


def main():
    app = QApplication(sys.argv)
    ui = Main_ui()
    ui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
 
