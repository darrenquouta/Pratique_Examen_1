# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_Medicament.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(946, 654)
        self.labelCode = QtWidgets.QLabel(Dialog)
        self.labelCode.setGeometry(QtCore.QRect(20, 20, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelCode.setFont(font)
        self.labelCode.setObjectName("labelCode")
        self.labelNomChimique = QtWidgets.QLabel(Dialog)
        self.labelNomChimique.setGeometry(QtCore.QRect(20, 140, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelNomChimique.setFont(font)
        self.labelNomChimique.setObjectName("labelNomChimique")
        self.labelNomCommercial = QtWidgets.QLabel(Dialog)
        self.labelNomCommercial.setGeometry(QtCore.QRect(20, 260, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelNomCommercial.setFont(font)
        self.labelNomCommercial.setObjectName("labelNomCommercial")
        self.labelCategorie = QtWidgets.QLabel(Dialog)
        self.labelCategorie.setGeometry(QtCore.QRect(400, 10, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelCategorie.setFont(font)
        self.labelCategorie.setObjectName("labelCategorie")
        self.labelPrix = QtWidgets.QLabel(Dialog)
        self.labelPrix.setGeometry(QtCore.QRect(20, 380, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPrix.setFont(font)
        self.labelPrix.setObjectName("labelPrix")
        self.labelPriseMaximale = QtWidgets.QLabel(Dialog)
        self.labelPriseMaximale.setGeometry(QtCore.QRect(660, 150, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPriseMaximale.setFont(font)
        self.labelPriseMaximale.setObjectName("labelPriseMaximale")
        self.labelDuree = QtWidgets.QLabel(Dialog)
        self.labelDuree.setGeometry(QtCore.QRect(660, 20, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelDuree.setFont(font)
        self.labelDuree.setObjectName("labelDuree")
        self.labelEffet = QtWidgets.QLabel(Dialog)
        self.labelEffet.setGeometry(QtCore.QRect(660, 270, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelEffet.setFont(font)
        self.labelEffet.setObjectName("labelEffet")
        self.pushButtonAjouter = QtWidgets.QPushButton(Dialog)
        self.pushButtonAjouter.setGeometry(QtCore.QRect(20, 590, 211, 51))
        self.pushButtonAjouter.setObjectName("pushButtonAjouter")
        self.pushButtonRechercher = QtWidgets.QPushButton(Dialog)
        self.pushButtonRechercher.setGeometry(QtCore.QRect(290, 590, 211, 51))
        self.pushButtonRechercher.setObjectName("pushButtonRechercher")
        self.lineEditCode = QtWidgets.QLineEdit(Dialog)
        self.lineEditCode.setGeometry(QtCore.QRect(20, 60, 271, 41))
        self.lineEditCode.setObjectName("lineEditCode")
        self.lineEditNomChimique = QtWidgets.QLineEdit(Dialog)
        self.lineEditNomChimique.setGeometry(QtCore.QRect(20, 180, 271, 41))
        self.lineEditNomChimique.setObjectName("lineEditNomChimique")
        self.lineEditDuree = QtWidgets.QLineEdit(Dialog)
        self.lineEditDuree.setGeometry(QtCore.QRect(660, 70, 271, 41))
        self.lineEditDuree.setObjectName("lineEditDuree")
        self.lineEditPriseMaximale = QtWidgets.QLineEdit(Dialog)
        self.lineEditPriseMaximale.setGeometry(QtCore.QRect(660, 190, 271, 41))
        self.lineEditPriseMaximale.setObjectName("lineEditPriseMaximale")
        self.lineEditPrix = QtWidgets.QLineEdit(Dialog)
        self.lineEditPrix.setGeometry(QtCore.QRect(20, 420, 271, 41))
        self.lineEditPrix.setObjectName("lineEditPrix")
        self.lineEditNomCommercial = QtWidgets.QLineEdit(Dialog)
        self.lineEditNomCommercial.setGeometry(QtCore.QRect(20, 300, 271, 41))
        self.lineEditNomCommercial.setObjectName("lineEditNomCommercial")
        self.comboBoxCategorie = QtWidgets.QComboBox(Dialog)
        self.comboBoxCategorie.setGeometry(QtCore.QRect(400, 60, 191, 41))
        self.comboBoxCategorie.setObjectName("comboBoxCategorie")
        self.comboBoxCategorie.addItem("")
        self.comboBoxCategorie.addItem("")
        self.comboBoxCategorie.addItem("")
        self.comboBoxEffet = QtWidgets.QComboBox(Dialog)
        self.comboBoxEffet.setGeometry(QtCore.QRect(660, 310, 191, 41))
        self.comboBoxEffet.setObjectName("comboBoxEffet")
        self.comboBoxEffet.addItem("")
        self.comboBoxEffet.addItem("")
        self.comboBoxEffet.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelCode.setText(_translate("Dialog", "Code du médicament"))
        self.labelNomChimique.setText(_translate("Dialog", "Nom chimique du médicament"))
        self.labelNomCommercial.setText(_translate("Dialog", "Nom commercial"))
        self.labelCategorie.setText(_translate("Dialog", "Catégorie"))
        self.labelPrix.setText(_translate("Dialog", "Prix"))
        self.labelPriseMaximale.setText(_translate("Dialog", "Prise quotidienne maximale"))
        self.labelDuree.setText(_translate("Dialog", "Durée de prise maximale"))
        self.labelEffet.setText(_translate("Dialog", "Effet du médicament"))
        self.pushButtonAjouter.setText(_translate("Dialog", "Ajouter"))
        self.pushButtonRechercher.setText(_translate("Dialog", "Rechercher"))
        self.comboBoxCategorie.setItemText(0, _translate("Dialog", "Antibiotique"))
        self.comboBoxCategorie.setItemText(1, _translate("Dialog", "Analgésique"))
        self.comboBoxCategorie.setItemText(2, _translate("Dialog", "Corticoïde"))
        self.comboBoxEffet.setItemText(0, _translate("Dialog", "Court"))
        self.comboBoxEffet.setItemText(1, _translate("Dialog", "Intermédiaire"))
        self.comboBoxEffet.setItemText(2, _translate("Dialog", "Prolongé"))
