from exceptions import NullException
from input import Ui_Dialog
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDateEdit,
    QDialog, QDialogButtonBox, QLabel, QSizePolicy,
    QTextEdit, QWidget)

class InputWindow(Ui_Dialog):
    def __init__(self):
        super(Ui_Dialog).__init__()
        self.buttonBox.accepted.connect(self.btn_accept)


    def btn_accept(self):
        try:
            self.type = self.cbx.currentText()
            if not self.type:
                raise NullException
            self.subtype = self.tbIncome.toPlainText()
            if not self.subtype:
                raise NullException
            self.cost = float(self.tbCost.toPlainText())
            if self.cost <= 0:
                raise ValueError
            if not self.cost:
                raise NullException
            self.transaction_date = self.dt.date().toPython()
            if not self.transaction_date:
                raise NullException
            self.ok = True
        except ValueError as e:
            print(e)
            self.Error = True
            return
        except NullException as n:
            print(n)
            self.Error = True
            return

class Dialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)