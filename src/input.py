# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogue.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from classes.exceptions import NullException
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDateEdit,
    QDialog, QDialogButtonBox, QLabel, QSizePolicy,
    QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(555, 358)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 300, 351, 41))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.tbIncome = QTextEdit(Dialog)
        self.tbIncome.setObjectName(u"tbIncome")
        self.tbIncome.setGeometry(QRect(70, 120, 371, 41))
        font = QFont()
        font.setPointSize(14)
        self.tbIncome.setFont(font)
        self.tbCost = QTextEdit(Dialog)
        self.tbCost.setObjectName(u"tbCost")
        self.tbCost.setGeometry(QRect(70, 180, 371, 41))
        self.tbCost.setFont(font)
        self.cbx = QComboBox(Dialog)
        self.cbx.addItem("")
        self.cbx.addItem("")
        self.cbx.setObjectName(u"cbx")
        self.cbx.setGeometry(QRect(150, 70, 191, 31))
        self.cbx.setFont(font)
        self.dt = QDateEdit(Dialog)
        self.dt.setObjectName(u"dt")
        self.dt.setGeometry(QRect(70, 240, 371, 23))
        self.dt.setFont(font)
        self.lblTransaction = QLabel(Dialog)
        self.lblTransaction.setObjectName(u"lblTransaction")
        self.lblTransaction.setGeometry(QRect(190, 20, 141, 41))
        font1 = QFont()
        font1.setPointSize(16)
        self.lblTransaction.setFont(font1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.accepted.connect(self.btn_accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.tbIncome.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u043e\u0434\u0442\u0438\u043f:", None))
        self.tbCost.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0446\u0435\u043d\u0443: ", None))
        self.cbx.setItemText(0, QCoreApplication.translate("Dialog", u"\u0414\u043e\u0445\u043e\u0434", None))
        self.cbx.setItemText(1, QCoreApplication.translate("Dialog", u"\u0420\u0430\u0441\u0445\u043e\u0434", None))

        self.lblTransaction.setText(QCoreApplication.translate("Dialog", u"\u0422\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u0438", None))
    # retranslateUi

    def btn_accept(self):
        try:
            self.type = self.cbx.currentText()
            if not self.type:
                raise NullException
            self.subtype = self.tbIncome.toPlainText()
            if not self.subtype:
                raise NullException
            self.cost = float(self.tbCost.toPlainText())
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

