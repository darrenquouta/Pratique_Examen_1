import Fichiers_PY.Dialog_Medicament
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from Classes.Medicament import Medicament
from Classes.Antibiotique import Antibiotique
from Classes.Analgesique import Analgesique
from Classes.Corticoide import Corticoide

class page_medicament(QtWidgets.QDialog, Fichiers_PY.Dialog_Medicament.Ui_Dialog):

    def __init__(self, parent=None):
        super(page_medicament, self).__init__(parent)
        self.setupUi(self)
        self.labelPriseMaximale.setDisabled(True)
        self.lineEditPriseMaximale.setDisabled(True)
        self.labelEffet.setDisabled(True)
        self.comboBoxEffet.setDisabled(True)
        self.labelAjoutMedicament.setVisible(False)
        self.labelAjoutErreur.setVisible(False)
        self.labelExistePas.setVisible(False)
        self.comboBoxCategorie.currentIndexChanged.connect(self.type_medicament)

    def type_medicament(self):
        if self.comboBoxCategorie.currentText() == "Antibiotique":
            antibiotique = True
            analgesique = False
            corticoide = False
        if self.comboBoxCategorie.currentText() == "Analgésique":
            analgesique = True
            antibiotique = False
            corticoide = False
        if self.comboBoxCategorie.currentText() == "Corticoïde":
            corticoide = True
            antibiotique = False
            analgesique = False
        self.activation(antibiotique, analgesique, corticoide)

    def activation(self, antibiotique, analgesique, corticoide):
        self.labelDuree.setDisabled(not antibiotique)
        self.lineEditDuree.setDisabled(not antibiotique)
        self.labelPriseMaximale.setDisabled(not analgesique)
        self.lineEditPriseMaximale.setDisabled(not analgesique)
        self.labelEffet.setDisabled(not corticoide)
        self.comboBoxEffet.setDisabled(not corticoide)

    @pyqtSlot()
    def on_pushButtonAjouter_clicked(self):
        self.labelAjoutErreur.setVisible(False)
        self.labelAjoutMedicament.setVisible(False)
        self.labelExistePas.setVisible(False)
        if self.comboBoxCategorie.currentText() == "Antibiotique":
            antibiotique = Antibiotique()
            code_medicament = self.lineEditCode.text()
            nom_chimique = self.lineEditNomChimique.text()
            nom_commercial = self.lineEditNomCommercial.text()
            prix = self.lineEditPrix.text()
            erreur = False
            try:
                antibiotique.code_medicament = code_medicament.upper()
            except ValueError as error:
                self.labelErreurCode.setText(f"{error}")
                erreur = True
            try:
                antibiotique.nom_chimique = nom_chimique
            except ValueError as error:
                self.labelErreurNomChimique.setText(f"{error}")
                erreur = True
            try:
                antibiotique.nom_commercial = nom_commercial
            except ValueError as error:
                self.labelErreurNomCommercial.setText(f"{error}")
                erreur = True
            try:
                antibiotique.prix = float(prix)
            except ValueError as error:
                self.labelErreurPrix.setText(f"{error}")
                erreur = True
            antibiotique.categorie_medicament = self.comboBoxCategorie.currentText()
            duree_prise_maximale = self.lineEditDuree.text()
            try:
                antibiotique.duree_prise_maximale = int(duree_prise_maximale)
            except ValueError as error:
                self.labelErreurDuree.setText(f"{error}")
                erreur = True
            if erreur == True:
                self.lineEditCode.clear()
                self.lineEditNomChimique.clear()
                self.lineEditNomCommercial.clear()
                self.lineEditPrix.clear()
                self.lineEditDuree.clear()
                self.lineEditPriseMaximale.clear()
                return None
            else:
                self.lineEditCode.clear()
                self.lineEditNomChimique.clear()
                self.lineEditNomCommercial.clear()
                self.lineEditPrix.clear()
                self.lineEditDuree.clear()
                self.lineEditPriseMaximale.clear()
                for medicament in Medicament.liste_medicaments:
                    if medicament.code_medicament == code_medicament:
                        self.labelAjoutErreur.setVisible(True)
                        return None
                else:
                    Medicament.liste_medicaments.append(antibiotique)
                    self.labelAjoutMedicament.setVisible(True)
        elif self.comboBoxCategorie.currentText() == "Analgésique":
            analgesique = Analgesique()
            code_medicament = self.lineEditCode.text()
            nom_chimique = self.lineEditNomChimique.text()
            nom_commercial = self.lineEditNomCommercial.text()
            prix = self.lineEditPrix.text()
            erreur = False
            try:
                analgesique.code_medicament = code_medicament.upper()
            except ValueError as error:
                self.labelErreurCode.setText(f"{error}")
                erreur = True
            try:
                analgesique.nom_chimique = nom_chimique
            except ValueError as error:
                self.labelErreurNomChimique.setText(f"{error}")
                erreur = True
            try:
                analgesique.nom_commercial = nom_commercial
            except ValueError as error:
                self.labelErreurNomCommercial.setText(f"{error}")
                erreur = True
            try:
                analgesique.prix = float(prix)
            except ValueError as error:
                self.labelErreurPrix.setText(f"{error}")
                erreur = True
            analgesique.categorie_medicament = self.comboBoxCategorie.currentText()
            prise_maximale = self.lineEditPriseMaximale.text()
            try:
                analgesique.prise_quotidienne_maximale = int(prise_maximale)
            except ValueError as error:
                self.labelErreurPrise.setText(f"{error}")
            if erreur == True:
                self.lineEditCode.clear()
                self.lineEditNomChimique.clear()
                self.lineEditNomCommercial.clear()
                self.lineEditPrix.clear()
                self.lineEditDuree.clear()
                self.lineEditPriseMaximale.clear()
                return None
            else:
                self.lineEditCode.clear()
                self.lineEditNomChimique.clear()
                self.lineEditNomCommercial.clear()
                self.lineEditPrix.clear()
                self.lineEditDuree.clear()
                self.lineEditPriseMaximale.clear()
                for medicament in Medicament.liste_medicaments:
                    if medicament.code_medicament == code_medicament:
                        self.labelAjoutErreur.setVisible(True)
                        return None
                else:
                    Medicament.liste_medicaments.append(analgesique)
                    self.labelAjoutMedicament.setVisible(True)
        else:
            corticoide = Corticoide()
            code_medicament = self.lineEditCode.text()
            nom_chimique = self.lineEditNomChimique.text()
            nom_commercial = self.lineEditNomCommercial.text()
            prix = self.lineEditPrix.text()
            erreur = False
            try:
                corticoide.code_medicament = code_medicament.upper()
            except ValueError as error:
                self.labelErreurCode.setText(f"{error}")
                erreur = True
            try:
                corticoide.nom_chimique = nom_chimique
            except ValueError as error:
                self.labelErreurNomChimique.setText(f"{error}")
                erreur = True
            try:
                corticoide.nom_commercial = nom_commercial
            except ValueError as error:
                self.labelErreurNomCommercial.setText(f"{error}")
                erreur = True
            try:
                corticoide.prix = float(prix)
            except ValueError as error:
                self.labelErreurPrix.setText(f"{error}")
                erreur = True
            corticoide.effet_medicament = self.comboBoxEffet.currentText()
            if erreur == True:
                self.lineEditCode.clear()
                self.lineEditNomChimique.clear()
                self.lineEditNomCommercial.clear()
                self.lineEditPrix.clear()
                self.lineEditDuree.clear()
                self.lineEditPriseMaximale.clear()
                return None
            else:
                self.lineEditCode.clear()
                self.lineEditNomChimique.clear()
                self.lineEditNomCommercial.clear()
                self.lineEditPrix.clear()
                self.lineEditDuree.clear()
                self.lineEditPriseMaximale.clear()
                for medicament in Medicament.liste_medicaments:
                    if medicament.code_medicament == code_medicament:
                        self.labelAjoutErreur.setVisible(True)
                        return None
                else:
                    Medicament.liste_medicaments.append(corticoide)
                    self.labelAjoutMedicament.setVisible(True)

    @pyqtSlot()
    def on_pushButtonRechercher_clicked(self):
        self.labelAjoutErreur.setVisible(False)
        self.labelAjoutMedicament.setVisible(False)
        self.labelExistePas.setVisible(False)
        code = self.lineEditCode.text()
        for medicament in Medicament.liste_medicaments:
            if medicament.code_medicament == code:
                self.lineEditNomChimique.setText(medicament.nom_chimique)
                self.lineEditNomCommercial.setText(medicament.nom_commercial)
                self.lineEditPrix.setText(str(medicament.prix))
                self.comboBoxCategorie.setCurrentText(medicament.categorie_medicament)
                if medicament.categorie_medicament == "Antibiotique":
                    self.lineEditDuree.setText(str(medicament.duree_prise_maximale))
                elif medicament.categorie_medicament == "Analgésique":
                    self.lineEditPriseMaximale.setText(str(medicament.prise_quotidienne_maximale))
                else:
                    self.comboBoxEffet.setCurrentText(medicament.effet_medicament)
                break
        else:
            self.labelExistePas.setVisible(True)




