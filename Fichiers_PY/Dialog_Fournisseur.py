# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_Fournisseur.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(845, 587)
        self.labelCode = QtWidgets.QLabel(Dialog)
        self.labelCode.setGeometry(QtCore.QRect(20, 20, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelCode.setFont(font)
        self.labelCode.setObjectName("labelCode")
        self.labelNom = QtWidgets.QLabel(Dialog)
        self.labelNom.setGeometry(QtCore.QRect(20, 120, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelNom.setFont(font)
        self.labelNom.setObjectName("labelNom")
        self.comboBoxPatient = QtWidgets.QComboBox(Dialog)
        self.comboBoxPatient.setGeometry(QtCore.QRect(580, 50, 231, 41))
        self.comboBoxPatient.setObjectName("comboBoxPatient")
        self.labelPatient = QtWidgets.QLabel(Dialog)
        self.labelPatient.setGeometry(QtCore.QRect(580, 20, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPatient.setFont(font)
        self.labelPatient.setObjectName("labelPatient")
        self.pushButtonSerialisation = QtWidgets.QPushButton(Dialog)
        self.pushButtonSerialisation.setGeometry(QtCore.QRect(80, 250, 171, 31))
        self.pushButtonSerialisation.setObjectName("pushButtonSerialisation")
        self.pushButtonDeserialisation = QtWidgets.QPushButton(Dialog)
        self.pushButtonDeserialisation.setGeometry(QtCore.QRect(80, 290, 171, 31))
        self.pushButtonDeserialisation.setObjectName("pushButtonDeserialisation")
        self.listViewPatient = QtWidgets.QListView(Dialog)
        self.listViewPatient.setGeometry(QtCore.QRect(270, 250, 541, 291))
        self.listViewPatient.setObjectName("listViewPatient")
        self.lineEditCode = QtWidgets.QLineEdit(Dialog)
        self.lineEditCode.setGeometry(QtCore.QRect(20, 50, 271, 41))
        self.lineEditCode.setObjectName("lineEditCode")
        self.lineEditNom = QtWidgets.QLineEdit(Dialog)
        self.lineEditNom.setGeometry(QtCore.QRect(20, 160, 271, 41))
        self.lineEditNom.setObjectName("lineEditNom")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelCode.setText(_translate("Dialog", "Code du fournisseur"))
        self.labelNom.setText(_translate("Dialog", "Nom de la compagnie"))
        self.labelPatient.setText(_translate("Dialog", "Patient"))
        self.pushButtonSerialisation.setText(_translate("Dialog", "Sérialiser fournisseur"))
        self.pushButtonDeserialisation.setText(_translate("Dialog", "Désérialiser fournisseur"))
