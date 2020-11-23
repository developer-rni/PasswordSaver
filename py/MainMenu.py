# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import py.DatabaseCreation
import py.AddingData
import py.StartWindow

import pprint


def connectsql(connected):
    if connected:
        print('connectsql')
        global conn
        global cur
        conn = sqlite3.connect(py.StartWindow.db_info[0])
        cur = conn.cursor()
        return True
    else:
        return False


def show_msg(text_show, text2_show):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(text_show)
    msg.setInformativeText(text2_show)
    msg.setWindowTitle("Сообщение")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.No)
    result = msg.exec_()
    return result


class Ui_MainWindow(object):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.createdb = createdb()
        self.addingdata = addingdata()

    def setupUi(self, MainWindow):
        MainWindow.resize(870, 600)
        MainWindow.setMinimumSize(QtCore.QSize(870, 600))
        MainWindow.setMaximumSize(QtCore.QSize(870, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 0, 190, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(10, 80, 830, 451))
        self.treeWidget.setAnimated(True)
        self.treeWidget.setObjectName("treeWidget")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.treeWidget.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.treeWidget.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.treeWidget.headerItem().setFont(2, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.treeWidget.headerItem().setFont(3, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.treeWidget.headerItem().setFont(4, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.treeWidget.headerItem().setFont(5, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.treeWidget.headerItem().setFont(6, font)

        # item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)

        # brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        # brush.setStyle(QtCore.Qt.NoBrush)
        # item_0.setBackground(0, brush)
        # brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        # brush.setStyle(QtCore.Qt.NoBrush)
        # item_0.setBackground(1, brush)
        # brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        # brush.setStyle(QtCore.Qt.NoBrush)
        # item_0.setBackground(2, brush)
        # brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        # brush.setStyle(QtCore.Qt.NoBrush)
        # item_0.setBackground(3, brush)
        # brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        # brush.setStyle(QtCore.Qt.NoBrush)
        # item_0.setBackground(4, brush)
        # brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        # brush.setStyle(QtCore.Qt.NoBrush)
        # item_0.setBackground(5, brush)
        # brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        # brush.setStyle(QtCore.Qt.NoBrush)
        # item_0.setBackground(6, brush)

        # item_1 = QtWidgets.QTreeWidgetItem(item_0)
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)
        # item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)
        # item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)
        # item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)

        self.treeWidget.header().setDefaultSectionSize(118)
        self.treeWidget.header().setMinimumSectionSize(50)
        self.treeWidget.header().setStretchLastSection(True)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(530, 50, 311, 25))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(690, 20, 151, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(810, 540, 31, 20))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 870, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)
        self.menu.addAction(self.action_5)
        self.menu.addSeparator()
        self.menu.addAction(self.action_7)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.action_3.triggered.connect(self.savebd)
        self.action_4.triggered.connect(self.show_createdb)
        self.action_5.triggered.connect(self.loadbd)
        self.action_7.triggered.connect(self.exit)
        self.pushButton.clicked.connect(self.deletedata)
        self.pushButton_2.clicked.connect(self.show_addingdata)
        self.pushButton_3.clicked.connect(self.copybuffer)

    def retranslateUi(self, MainWindow):
        sqlcheck = connectsql(False)
        print(sqlcheck)
        if sqlcheck:
            [test_db_info], = cur.execute("SELECT name FROM account_information WHERE ID=2")
            print(test_db_info)

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Saver - Главная"))
        self.label.setText(_translate("MainWindow", "Password Saver"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Раздел"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Название"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Логин"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "Пароль"))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "Почта"))
        self.treeWidget.headerItem().setText(5, _translate("MainWindow", "Секретное слово"))
        self.treeWidget.headerItem().setText(6, _translate("MainWindow", "URL"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        # self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Почта"))
        # self.treeWidget.topLevelItem(0).child(0).setText(1, _translate("MainWindow", "yandex"))
        # self.treeWidget.topLevelItem(0).child(0).setText(2, _translate("MainWindow", "test@yandex.ru"))
        # self.treeWidget.topLevelItem(0).child(0).setText(3, _translate("MainWindow", "qwerty123"))
        # self.treeWidget.topLevelItem(0).child(0).setText(4, _translate("MainWindow", "test@yandex.ru"))
        # self.treeWidget.topLevelItem(0).child(0).setText(5, _translate("MainWindow", "123"))
        # self.treeWidget.topLevelItem(0).child(0).setText(6, _translate("MainWindow", "https://yandex.ru"))
        # self.treeWidget.topLevelItem(0).child(1).setText(1, _translate("MainWindow", "mail"))
        # self.treeWidget.topLevelItem(0).child(1).setText(2, _translate("MainWindow", "test@mail.ru"))
        # self.treeWidget.topLevelItem(0).child(1).setText(3, _translate("MainWindow", "ytrewq321"))
        # self.treeWidget.topLevelItem(0).child(1).setText(4, _translate("MainWindow", "test@mail.ru"))
        # self.treeWidget.topLevelItem(0).child(1).setText(5, _translate("MainWindow", "231"))
        # self.treeWidget.topLevelItem(0).child(1).setText(6, _translate("MainWindow", "https://mail.ru"))
        # self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "Игры"))
        # self.treeWidget.topLevelItem(1).child(0).setText(1, _translate("MainWindow", "testgame"))
        # self.treeWidget.topLevelItem(1).child(0).setText(2, _translate("MainWindow", "gamelogin"))
        # self.treeWidget.topLevelItem(1).child(0).setText(3, _translate("MainWindow", "gamepass123"))
        # self.treeWidget.topLevelItem(1).child(0).setText(4, _translate("MainWindow", "test@mail.ru"))
        # self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "Соц сети"))
        # self.treeWidget.topLevelItem(2).child(0).setText(1, _translate("MainWindow", "Vk"))
        # self.treeWidget.topLevelItem(2).child(0).setText(2, _translate("MainWindow", "loginvk"))
        # self.treeWidget.topLevelItem(2).child(0).setText(3, _translate("MainWindow", "vkpass123"))
        # self.treeWidget.topLevelItem(2).child(0).setText(4, _translate("MainWindow", "test@mail.ru"))
        # self.treeWidget.topLevelItem(2).child(0).setText(5, _translate("MainWindow", "231"))
        # self.treeWidget.topLevelItem(2).child(0).setText(6, _translate("MainWindow", "https://vk.com"))
        # self.treeWidget.topLevelItem(3).setText(0, _translate("MainWindow", "Разное"))
        # self.treeWidget.topLevelItem(3).child(0).setText(1, _translate("MainWindow", "Forum"))
        # self.treeWidget.topLevelItem(3).child(0).setText(2, _translate("MainWindow", "forumlogin"))
        # self.treeWidget.topLevelItem(3).child(0).setText(3, _translate("MainWindow", "ytrewq12345"))
        # self.treeWidget.topLevelItem(3).child(0).setText(4, _translate("MainWindow", "testyandexlong@yandex.ru"))
        # self.treeWidget.topLevelItem(3).child(0).setText(5, _translate("MainWindow", "213"))
        # self.treeWidget.topLevelItem(3).child(0).setText(6, _translate("MainWindow", "https://testforumnexttest.ru"))
        # self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_3.setText(_translate("MainWindow", "Копировать пароль в буфер"))
        self.pushButton.setText(_translate("MainWindow", "Удалить"))
        self.pushButton_2.setText(_translate("MainWindow", "Добавить"))
        self.label_2.setText(_translate("MainWindow", "v 0.2"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.action.setText(_translate("MainWindow", "Выход"))
        self.action_2.setText(_translate("MainWindow", "Сохранить"))
        self.action_3.setText(_translate("MainWindow", "Сохранить"))
        self.action_4.setText(_translate("MainWindow", "Создать новую БД"))
        self.action_5.setText(_translate("MainWindow", "Загрузить БД"))
        self.action_7.setText(_translate("MainWindow", "Выход"))

    def datafilling(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Почта"))
        self.treeWidget.topLevelItem(0).child(0).setText(1, _translate("MainWindow", "yandex"))
        self.treeWidget.topLevelItem(0).child(0).setText(2, _translate("MainWindow", "test@yandex.ru"))
        self.treeWidget.topLevelItem(0).child(0).setText(3, _translate("MainWindow", "qwerty123"))
        self.treeWidget.topLevelItem(0).child(0).setText(4, _translate("MainWindow", "test@yandex.ru"))
        self.treeWidget.topLevelItem(0).child(0).setText(5, _translate("MainWindow", "123"))
        self.treeWidget.topLevelItem(0).child(0).setText(6, _translate("MainWindow", "https://yandex.ru"))
        self.treeWidget.topLevelItem(0).child(1).setText(1, _translate("MainWindow", "mail"))
        self.treeWidget.topLevelItem(0).child(1).setText(2, _translate("MainWindow", "test@mail.ru"))
        self.treeWidget.topLevelItem(0).child(1).setText(3, _translate("MainWindow", "ytrewq321"))
        self.treeWidget.topLevelItem(0).child(1).setText(4, _translate("MainWindow", "test@mail.ru"))
        self.treeWidget.topLevelItem(0).child(1).setText(5, _translate("MainWindow", "231"))
        self.treeWidget.topLevelItem(0).child(1).setText(6, _translate("MainWindow", "https://mail.ru"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "Игры"))
        self.treeWidget.topLevelItem(1).child(0).setText(1, _translate("MainWindow", "testgame"))
        self.treeWidget.topLevelItem(1).child(0).setText(2, _translate("MainWindow", "gamelogin"))
        self.treeWidget.topLevelItem(1).child(0).setText(3, _translate("MainWindow", "gamepass123"))
        self.treeWidget.topLevelItem(1).child(0).setText(4, _translate("MainWindow", "test@mail.ru"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "Соц сети"))
        self.treeWidget.topLevelItem(2).child(0).setText(1, _translate("MainWindow", "Vk"))
        self.treeWidget.topLevelItem(2).child(0).setText(2, _translate("MainWindow", "loginvk"))
        self.treeWidget.topLevelItem(2).child(0).setText(3, _translate("MainWindow", "vkpass123"))
        self.treeWidget.topLevelItem(2).child(0).setText(4, _translate("MainWindow", "test@mail.ru"))
        self.treeWidget.topLevelItem(2).child(0).setText(5, _translate("MainWindow", "231"))
        self.treeWidget.topLevelItem(2).child(0).setText(6, _translate("MainWindow", "https://vk.com"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("MainWindow", "Разное"))
        self.treeWidget.topLevelItem(3).child(0).setText(1, _translate("MainWindow", "Forum"))
        self.treeWidget.topLevelItem(3).child(0).setText(2, _translate("MainWindow", "forumlogin"))
        self.treeWidget.topLevelItem(3).child(0).setText(3, _translate("MainWindow", "ytrewq12345"))
        self.treeWidget.topLevelItem(3).child(0).setText(4, _translate("MainWindow", "testyandexlong@yandex.ru"))
        self.treeWidget.topLevelItem(3).child(0).setText(5, _translate("MainWindow", "213"))
        self.treeWidget.topLevelItem(3).child(0).setText(6, _translate("MainWindow", "https://testforumnexttest.ru"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)


    @QtCore.pyqtSlot()
    def savebd(self):
        print('save')

    @QtCore.pyqtSlot()
    def show_createdb(self):
        self.createdb.show()

    @QtCore.pyqtSlot()
    def loadbd(self):
        print('loadbd')
        pass

    @QtCore.pyqtSlot()
    def exit(self):
        result = show_msg('Все несохраненные изменения будут потеряны.', 'Все равно выйти?')
        if result == 1024:
            self.close()
        elif result == 65536:
            pass

    @QtCore.pyqtSlot()
    def show_addingdata(self):
        self.addingdata.show()

    @QtCore.pyqtSlot()
    def copybuffer(self):
        print('copybuffer')
        pass

    @QtCore.pyqtSlot()
    def deletedata(self):
        print('deletedata')
        pass


class createdb(QtWidgets.QDialog, py.DatabaseCreation.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class addingdata(QtWidgets.QDialog, py.AddingData.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
