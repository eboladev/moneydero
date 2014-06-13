# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registro.ui'
#
# Created: Fri Jun 13 10:04:36 2014
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
        Frame.setAutoFillBackground(True)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        Frame.setLineWidth(1)
        Frame.setMidLineWidth(0)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(Frame)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
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
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_fecha = QtGui.QLabel(Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_fecha.sizePolicy().hasHeightForWidth())
        self.label_fecha.setSizePolicy(sizePolicy)
        self.label_fecha.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_fecha.setObjectName(_fromUtf8("label_fecha"))
        self.horizontalLayout.addWidget(self.label_fecha)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_cantidad = QtGui.QLabel(Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_cantidad.sizePolicy().hasHeightForWidth())
        self.label_cantidad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_cantidad.setFont(font)
        self.label_cantidad.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_cantidad.setObjectName(_fromUtf8("label_cantidad"))
        self.horizontalLayout_2.addWidget(self.label_cantidad)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_cuenta = QtGui.QLabel(Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_cuenta.sizePolicy().hasHeightForWidth())
        self.label_cuenta.setSizePolicy(sizePolicy)
        self.label_cuenta.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_cuenta.setObjectName(_fromUtf8("label_cuenta"))
        self.verticalLayout.addWidget(self.label_cuenta)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.pushButton = QtGui.QPushButton(Frame)
        self.pushButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("edit-delete"))
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(Frame)
        self.pushButton_2.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-edit"))
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_3.addWidget(self.pushButton_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

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

