# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registro.ui'
#
# Created: Mon Jun  2 12:06:04 2014
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

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(742, 225)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout = QtGui.QHBoxLayout(Frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_categoria = QtGui.QLabel(Frame)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_categoria.setFont(font)
        self.label_categoria.setObjectName(_fromUtf8("label_categoria"))
        self.verticalLayout_2.addWidget(self.label_categoria)
        self.label_concepto = QtGui.QLabel(Frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_concepto.setFont(font)
        self.label_concepto.setObjectName(_fromUtf8("label_concepto"))
        self.verticalLayout_2.addWidget(self.label_concepto)
        self.label_socio = QtGui.QLabel(Frame)
        self.label_socio.setObjectName(_fromUtf8("label_socio"))
        self.verticalLayout_2.addWidget(self.label_socio)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_fecha = QtGui.QLabel(Frame)
        self.label_fecha.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_fecha.setObjectName(_fromUtf8("label_fecha"))
        self.verticalLayout.addWidget(self.label_fecha)
        self.label_cantidad = QtGui.QLabel(Frame)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_cantidad.setFont(font)
        self.label_cantidad.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_cantidad.setObjectName(_fromUtf8("label_cantidad"))
        self.verticalLayout.addWidget(self.label_cantidad)
        self.label_cuenta = QtGui.QLabel(Frame)
        self.label_cuenta.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_cuenta.setObjectName(_fromUtf8("label_cuenta"))
        self.verticalLayout.addWidget(self.label_cuenta)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Frame", None))
        self.label_categoria.setText(_translate("Frame", "Coche", None))
        self.label_concepto.setText(_translate("Frame", "Reparación de golpe", None))
        self.label_socio.setText(_translate("Frame", "Fernando", None))
        self.label_fecha.setText(_translate("Frame", "1 de junio de 2014", None))
        self.label_cantidad.setText(_translate("Frame", "-50,00 €", None))
        self.label_cuenta.setText(_translate("Frame", "Efectivo", None))

