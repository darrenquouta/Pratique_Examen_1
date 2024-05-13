import Fichiers_PY.Dialog_Medicament
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot

class page_medicament(QtWidgets.QDialog, Fichiers_PY.Dialog_Medicament.Ui_Dialog):

    def __init__(self, parent=None):
        super(page_medicament, self).__init__(parent)
        self.setupUi(self)