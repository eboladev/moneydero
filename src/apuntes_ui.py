# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'apuntes.ui'
#
# Created: Mon Jun  2 09:23:04 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(828, 698)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_gasto = QtGui.QPushButton(Dialog)
        self.pushButton_gasto.setObjectName(_fromUtf8("pushButton_gasto"))
        self.horizontalLayout.addWidget(self.pushButton_gasto)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setWrapping(False)
        self.doubleSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox.setSpecialValueText(_fromUtf8(""))
        self.doubleSpinBox.setAccelerated(False)
        self.doubleSpinBox.setMinimum(0.0)
        self.doubleSpinBox.setMaximum(999999.99)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.horizontalLayout.addWidget(self.doubleSpinBox)
        self.comboBox_cuenta = QtGui.QComboBox(Dialog)
        self.comboBox_cuenta.setObjectName(_fromUtf8("comboBox_cuenta"))
        self.comboBox_cuenta.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.comboBox_cuenta)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 63, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.comboBox_categoria = QtGui.QComboBox(Dialog)
        self.comboBox_categoria.setEditable(False)
        self.comboBox_categoria.setObjectName(_fromUtf8("comboBox_categoria"))
        self.comboBox_categoria.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.comboBox_categoria)
        self.comboBox_vendedor = QtGui.QComboBox(Dialog)
        self.comboBox_vendedor.setEditable(True)
        self.comboBox_vendedor.setObjectName(_fromUtf8("comboBox_vendedor"))
        self.comboBox_vendedor.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.comboBox_vendedor)
        self.dateEdit_fecha = QtGui.QDateEdit(Dialog)
        self.dateEdit_fecha.setCalendarPopup(True)
        self.dateEdit_fecha.setObjectName(_fromUtf8("dateEdit_fecha"))
        self.horizontalLayout_2.addWidget(self.dateEdit_fecha)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.lineEdit_concepto = QtGui.QLineEdit(Dialog)
        self.lineEdit_concepto.setObjectName(_fromUtf8("lineEdit_concepto"))
        self.verticalLayout_2.addWidget(self.lineEdit_concepto)
        spacerItem2 = QtGui.QSpacerItem(20, 64, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.dateEdit_garantia = QtGui.QDateEdit(self.groupBox)
        self.dateEdit_garantia.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.dateEdit_garantia.setCalendarPopup(True)
        self.dateEdit_garantia.setObjectName(_fromUtf8("dateEdit_garantia"))
        self.verticalLayout.addWidget(self.dateEdit_garantia)
        self.pushButton_adjuntos = QtGui.QPushButton(self.groupBox)
        self.pushButton_adjuntos.setObjectName(_fromUtf8("pushButton_adjuntos"))
        self.verticalLayout.addWidget(self.pushButton_adjuntos)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.listWidget = QtGui.QListWidget(self.groupBox)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.horizontalLayout_4.addWidget(self.listWidget)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem3 = QtGui.QSpacerItem(20, 63, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton_cancelar = QtGui.QPushButton(Dialog)
        self.pushButton_cancelar.setObjectName(_fromUtf8("pushButton_cancelar"))
        self.horizontalLayout_3.addWidget(self.pushButton_cancelar)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.pushButton_guardar = QtGui.QPushButton(Dialog)
        self.pushButton_guardar.setObjectName(_fromUtf8("pushButton_guardar"))
        self.horizontalLayout_3.addWidget(self.pushButton_guardar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Introducir apunte", None))
        self.pushButton_gasto.setText(_translate("Dialog", "Gasto", None))
        self.doubleSpinBox.setPrefix(_translate("Dialog", "-", None))
        self.comboBox_cuenta.setItemText(0, _translate("Dialog", "Efectivo", None))
        self.comboBox_categoria.setItemText(0, _translate("Dialog", "Categoria", None))
        self.comboBox_vendedor.setItemText(0, _translate("Dialog", "Vendedor", None))
        self.lineEdit_concepto.setPlaceholderText(_translate("Dialog", "Concepto", None))
        self.groupBox.setTitle(_translate("Dialog", "Garantia", None))
        self.pushButton_adjuntos.setText(_translate("Dialog", "Archivos adjuntos", None))
        self.pushButton_cancelar.setText(_translate("Dialog", "Cancelar", None))
        self.pushButton_guardar.setText(_translate("Dialog", "Guardar", None))

