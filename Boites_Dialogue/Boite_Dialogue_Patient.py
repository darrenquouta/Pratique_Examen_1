import Fichiers_PY.Dialog_Patient
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot

class page_patient(QtWidgets.QDialog, Fichiers_PY.Dialog_Patient.Ui_Dialog):

    def __init__(self, parent=None):
        super(page_patient, self).__init__(parent)
        self.setupUi(self)