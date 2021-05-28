# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recommend.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(368, 175)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 361, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Recommend = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Recommend.setTextFormat(QtCore.Qt.AutoText)
        self.Recommend.setAlignment(QtCore.Qt.AlignCenter)
        self.Recommend.setObjectName("Recommend")
        self.verticalLayout.addWidget(self.Recommend)
        self.Description = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Description.setTextFormat(QtCore.Qt.AutoText)
        self.Description.setAlignment(QtCore.Qt.AlignCenter)
        self.Description.setObjectName("Description")
        self.verticalLayout.addWidget(self.Description)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 368, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Recommend.setText(_translate("MainWindow", "Hewan"))
        self.Description.setText(_translate("MainWindow", "TextLabel"))
