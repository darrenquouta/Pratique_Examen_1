import Fichiers_PY.Dialog_Patient
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from Classes.Patient import Patient


class page_patient(QtWidgets.QDialog, Fichiers_PY.Dialog_Patient.Ui_Dialog):

    def __init__(self, parent=None):
        super(page_patient, self).__init__(parent)
        self.setupUi(self)
        self.labelAjout.setVisible(False)
        self.labelAjoutRefuse.setVisible(False)
        self.labelExistePas.setVisible(False)
        self.labelSupprime.setVisible(False)

    @pyqtSlot()
    def on_pushButtonAjouterPatient_clicked(self):
        self.labelAjout.setVisible(False)
        self.labelAjoutRefuse.setVisible(False)
        self.labelExistePas.setVisible(False)
        self.labelSupprime.setVisible(False)
        patient = Patient()
        numero_patient = self.lineEditNumero.text()
        nom_patient = self.lineEditNom.text()
        prenom_patient = self.lineEditPrenom.text()
        erreur = False
        try:
            patient.numero_patient = numero_patient
        except ValueError as error:
            self.labelErreurNumero.setText(f"{error}")
            erreur = True
        try:
            patient.nom_famille = nom_patient
        except ValueError as error:
            self.labelErreurNom.setText(f"{error}")
            erreur = True
        try:
            patient.prenom = prenom_patient
        except ValueError as error:
            self.labelErreurPrenom.setText(f"{error}")
            erreur = True
        patient.date_naissance = self.dateEditDateNaissance.date().toPyDate()
        if erreur == True:
            self.lineEditNumero.clear()
            self.lineEditNom.clear()
            self.lineEditPrenom.clear()
            return None
        if erreur == False:
            for patient in Patient.liste_patients:
                if patient.numero_patient == numero_patient:
                    self.labelAjoutRefuse.setVisible(True)
                    return None
            else:
                Patient.liste_patients.append(patient)
                self.labelAjout.setVisible(True)

    @pyqtSlot()
    def on_pushButtonSupprimerPatient_clicked(self):
        self.labelAjout.setVisible(False)
        self.labelAjoutRefuse.setVisible(False)
        self.labelExistePas.setVisible(False)
        self.labelSupprime.setVisible(False)
        numero_patient = self.lineEditNumero.text()
        nom_patient = self.lineEditNom.text()
        prenom_patient = self.lineEditPrenom.text()
        date_naissance = self.dateEditDateNaissance.date().toPyDate()
        for patient in Patient.liste_patients:
            if (patient.numero_patient == numero_patient and patient.nom_famille == nom_patient and
                    patient.prenom == prenom_patient and patient.date_naissance == date_naissance):
                Patient.liste_patients.remove(patient)
                self.labelSupprime.setVisible(True)
                return None
        else:
            self.labelExistePas.setVisible(True)

