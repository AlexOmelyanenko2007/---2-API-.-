# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'API.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(941, 591)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.map = QtWidgets.QLabel(self.centralwidget)
        self.map.setText("")
        self.map.setObjectName("map")
        self.verticalLayout.addWidget(self.map)
        self.address = QtWidgets.QLineEdit(self.centralwidget)
        self.address.setObjectName("address")
        self.verticalLayout.addWidget(self.address)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scheme = QtWidgets.QRadioButton(self.centralwidget)
        self.scheme.setObjectName("scheme")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.scheme)
        self.verticalLayout_2.addWidget(self.scheme)
        self.sputnik = QtWidgets.QRadioButton(self.centralwidget)
        self.sputnik.setObjectName("sputnik")
        self.buttonGroup.addButton(self.sputnik)
        self.verticalLayout_2.addWidget(self.sputnik)
        self.hybrid = QtWidgets.QRadioButton(self.centralwidget)
        self.hybrid.setObjectName("hybrid")
        self.buttonGroup.addButton(self.hybrid)
        self.verticalLayout_2.addWidget(self.hybrid)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.search_bar.setObjectName("search_bar")
        self.horizontalLayout.addWidget(self.search_bar)
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setObjectName("search")
        self.horizontalLayout.addWidget(self.search)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.is_postal_code = QtWidgets.QCheckBox(self.centralwidget)
        self.is_postal_code.setObjectName("is_postal_code")
        self.horizontalLayout_2.addWidget(self.is_postal_code)
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout_2.addWidget(self.clear_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.scheme.setText(_translate("MainWindow", "Scheme"))
        self.sputnik.setText(_translate("MainWindow", "Sputnik"))
        self.hybrid.setText(_translate("MainWindow", "Hybrid"))
        self.search.setText(_translate("MainWindow", "Search"))
        self.is_postal_code.setText(_translate("MainWindow", "CheckBox"))
        self.clear_btn.setText(_translate("MainWindow", "Clear"))
