import Fichiers_PY.Page_Principale
from Boites_Dialogue.Boite_Dialogue_Fournisseur import page_fournisseur
from Boites_Dialogue.Boite_Dialogue_Patient import page_patient
from Boites_Dialogue.Boite_Dialogue_Medicament import page_medicament
from Boites_Dialogue.Boite_Dialogue_Recherche import page_recherche
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot

class pageAccueil(QtWidgets.QMainWindow, Fichiers_PY.Page_Principale.Ui_MainWindow):

    def __init__(self, parent=None):
        super(pageAccueil, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButtonFournisseur_clicked(self):
        dialogue = page_fournisseur()
        dialogue.show()
        dialogue.exec_()

    @pyqtSlot()
    def on_pushButtonPatient_clicked(self):
        dialogue = page_patient()
        dialogue.show()
        dialogue.exec_()

    @pyqtSlot()
    def on_pushButtonMedicament_clicked(self):
        dialogue = page_medicament()
        dialogue.show()
        dialogue.exec_()

    @pyqtSlot()
    def on_pushButtonRecherche_clicked(self):
        dialogue = page_recherche()
        dialogue.show()
        dialogue.exec_()

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = pageAccueil()
    form.show()
    app.exec()

if __name__ == "__main__":
    main()
