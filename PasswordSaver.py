#!/usr/bin/python3
# Password Saver by Rybkin Nikita Igorevich
# -*- coding: utf-8 -*-
# v 0.1

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QWidget
import py.MainMenu
import py.StartWindow
import py.DatabaseCreation

version = 'v 0.1'


class Interface(QtWidgets.QDialog, py.StartWindow.Ui_Dialog):
    def __init__(self):
        super(Interface, self).__init__()
        self.setupUi(self)

        self.mainwindow = mainwindow()
        self.createdb = createdb()
        self.InitUI()

    def InitUI(self):
        self.pushButton_3.clicked.connect(self.show_mainwindow)
        self.pushButton_2.clicked.connect(self.show_createdb)

    def show_mainwindow(self):
        iw = bool(1)
        if iw:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Оповещение")
            msg.setText("Успешный вход")
            msg.exec_()
            self.mainwindow.show()
            self.hide()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Ошибка входа")
            msg.setText("Неправильный пароль")
            msg.exec_()

    def show_createdb(self):
        self.close()
        self.createdb.show()


class mainwindow(QtWidgets.QMainWindow, py.MainMenu.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class createdb(QtWidgets.QDialog, py.DatabaseCreation.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Interface()
    window.show()
    sys.exit(app.exec_())
