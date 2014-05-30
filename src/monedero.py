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


from PyQt4 import QtCore
from PyQt4.QtGui import QApplication, QMainWindow, QListWidgetItem, QPixmap, QInputDialog, QMenu, QAction
from monedero_ui import Ui_MainWindow



class Main_ui(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main_ui, self).__init__()
        self.setupUi(self)

        


def main():
    app = QApplication(sys.argv)
    ui = Main_ui()
    ui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
 
