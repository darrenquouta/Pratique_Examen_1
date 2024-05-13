import Fichiers_PY.Dialog_Fournisseur
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot

class page_fournisseur(QtWidgets.QDialog, Fichiers_PY.Dialog_Fournisseur.Ui_Dialog):

    def __init__(self, parent=None):
        super(page_fournisseur, self).__init__(parent)
        self.setupUi(self)
