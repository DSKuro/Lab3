# -*- coding: utf-8 -*-
from classes.exceptions import NullException
from classes.transaction import Transactions
from classes.budget import Budget
from input import Dialog
import os

import pyqtgraph as pg

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHeaderView, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QTextEdit, QWidget, QVBoxLayout, QGridLayout)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.temp_list = list()
        self.table_rows = 0
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(912, 600)
        self.actionAdd = QAction(MainWindow)
        self.actionAdd.setObjectName(u"actionAdd")
        self.actionAdd.triggered.connect(self.btn_action_click)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblName = QLabel(self.centralwidget)
        self.lblName.setObjectName(u"lblName")
        self.lblName.setGeometry(QRect(260, 10, 341, 41))
        font = QFont()
        font.setPointSize(18)
        self.lblName.setFont(font)
        self.table = QTableWidget(self.centralwidget)
        if (self.table.columnCount() < 2):
            self.table.setColumnCount(2)
        font1 = QFont()
        font1.setPointSize(14)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.table.rowCount() < 1):
            self.table.setRowCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.table.setItem(0, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.table.setItem(0, 1, __qtablewidgetitem4)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(10, 60, 401, 71))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.setMinimumSize(QSize(1, 1))
        self.table.setBaseSize(QSize(1, 1))
        self.table.setColumnWidth(1, 450)
        self.table.setWordWrap(True)
        self.graph = QGraphicsView(self.centralwidget)
        self.graph.setObjectName(u"graph")
        self.graph.setGeometry(QRect(460, 90, 441, 321))
        self.btnRun = QPushButton(self.centralwidget)
        self.btnRun.setObjectName(u"btnRun")
        self.btnRun.setGeometry(QRect(20, 470, 141, 51))
        self.btnRun.setFont(font1)
        self.btnRun.clicked.connect(self.btn_run)
        self.btnLog = QPushButton(self.centralwidget)
        self.btnLog.setObjectName(u"btnLog")
        self.btnLog.setGeometry(QRect(190, 470, 141, 51))
        self.btnLog.setFont(font1)
        self.btnLog.clicked.connect(self.btn_log)
        self.tableResult = QTableWidget(self.centralwidget)
        if (self.tableResult.columnCount() < 4):
            self.tableResult.setColumnCount(4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.tableResult.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font1);
        self.tableResult.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font1);
        self.tableResult.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font1);
        self.tableResult.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        if (self.tableResult.rowCount() < 9):
            self.tableResult.setRowCount(9)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableResult.setVerticalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableResult.setVerticalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableResult.setVerticalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableResult.setVerticalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableResult.setVerticalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableResult.setVerticalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableResult.setVerticalHeaderItem(6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableResult.setVerticalHeaderItem(7, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableResult.setVerticalHeaderItem(8, __qtablewidgetitem17)
        self.tableResult.setObjectName(u"tableResult")
        self.tableResult.setGeometry(QRect(10, 140, 411, 141))
        self.txtStart = QTextEdit(self.centralwidget)
        self.txtStart.setObjectName(u"txtStart")
        self.txtStart.setGeometry(QRect(10, 320, 411, 41))
        self.txtStart.setFont(font1)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(480, 70, 411, 421))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 912, 33))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionAdd)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setGeometry(0, 0, 400, 300)

        self.graphWidget.setBackground('w')

        self.gridLayout.addWidget(self.graphWidget)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAdd.setText(
            QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c ", None))
        self.lblName.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0424\u0438\u043d\u0430\u043d\u0441\u043e\u0432\u044b\u0439 \u0442\u0440\u0435\u043a\u0435\u0440 \u0440\u0430\u0441\u0445\u043e\u0434\u043e\u0432",
                                                        None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u2116", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0440\u0438\u0430\u043d\u0442", None));

        __sortingEnabled = self.table.isSortingEnabled()
        self.table.setSortingEnabled(False)
        ___qtablewidgetitem2 = self.table.item(0, 0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem3 = self.table.item(0, 1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u0424\u0438\u043d\u0430\u043d\u0441\u043e\u0432\u044b\u0439 \u0442\u0440\u0435\u043a\u0435\u0440 \u0440\u0430\u0441\u0445\u043e\u0434\u043e\u0432",
                                                                None));
        self.table.setSortingEnabled(__sortingEnabled)

        self.btnRun.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        self.btnLog.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433", None))
        ___qtablewidgetitem4 = self.tableResult.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem5 = self.tableResult.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"SubType", None));
        ___qtablewidgetitem6 = self.tableResult.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Cost", None));
        ___qtablewidgetitem7 = self.tableResult.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        self.txtStart.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                    u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u0442\u0430\u0440\u0442\u043e\u0432\u044b\u0439 \u0431\u044e\u0434\u0436\u0435\u0442",
                                                                    None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
    # retranslateUi

    def add_to_table(self, transaction : Transactions):
        temp = list()
        temp.append(str(transaction.type))
        temp.append(str(transaction.type_income))
        temp.append(str(transaction.cost))
        temp.append(str(transaction.date))
        for i in range(0, 4):
            item = QTableWidgetItem()
            self.tableResult.setItem(self.table_rows, i, item)
            item.setText(temp[i])
        self.table_rows += 1

    def btn_action_click(self):
        print(self.table.rowCount)
        dlg = Dialog()
        dlg.exec()
        if dlg.ok:
            transaction = Transactions(dlg.type, dlg.subtype, dlg.cost, dlg.transaction_date)
            self.temp_list.append(transaction)
            self.add_to_table(transaction)

    def get_cost(self) -> list:
        costs = list()
        for i in self.temp_list:
            costs.append(i.cost)
        return costs

    def get_dates(self) -> list:
        dates = list()
        for i in self.temp_list:
            dates.append(i.date.day)
        return dates

    def btn_run(self):
        try:
            st_b = float(self.txtStart.toPlainText())
            if st_b <= 0.0:
                raise ValueError
            if not st_b:
                raise NullException
        except ValueError as e:
            print(e)
            return
        except NullException as n:
            print(n)
            return
        self.budget = Budget(st_b, self.temp_list)
        self.budget.calculate_budget()

        print("yes")
        costs = self.get_cost()
        dates = self.get_dates()
        print("no")
        print(costs, dates)
        pen = pg.mkPen(color=(255, 0, 0))
        self.graphWidget.plot(costs, dates, pen=pen)
        self.run = True

    def btn_log(self):
        if not self.run:
            print("Нечего выводить!")
            return
        file = open("log.txt", "a+")
        check_file = os.stat("log.txt").st_size

        if (check_file != 0):
            file.write("\n")
        file.write(str(self.budget))
        file.close()



