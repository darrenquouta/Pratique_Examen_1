import Fichiers_PY.Dialog_Recherche
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot

class page_recherche(QtWidgets.QDialog, Fichiers_PY.Dialog_Recherche.Ui_Dialog):

    def __init__(self, parent=None):
        super(page_recherche, self).__init__(parent)
        self.setupUi(self)