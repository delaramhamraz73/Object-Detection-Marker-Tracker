# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(590, 584)
        MainWindow.setStyleSheet("background-image: url(:/images/1.jpg);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.chooseButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseButton.setAutoFillBackground(False)
        self.chooseButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.chooseButton.setObjectName("chooseButton")
        self.horizontalLayout_4.addWidget(self.chooseButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setAutoFillBackground(False)
        self.playButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.playButton.setObjectName("playButton")
        self.verticalLayout_3.addWidget(self.playButton)
        self.verticalLayout_8.addLayout(self.verticalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_2.addWidget(self.radioButton, 0, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_2.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout_2.addWidget(self.radioButton_3, 2, 0, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout_2.addWidget(self.radioButton_4, 3, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_6.addWidget(self.groupBox)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.maskButton = QtWidgets.QPushButton(self.centralwidget)
        self.maskButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.maskButton.setObjectName("maskButton")
        self.verticalLayout_7.addWidget(self.maskButton)
        self.trackButton = QtWidgets.QPushButton(self.centralwidget)
        self.trackButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.trackButton.setObjectName("trackButton")
        self.verticalLayout_7.addWidget(self.trackButton)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.gridLayout_5.addLayout(self.verticalLayout_8, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_8.setObjectName("radioButton_8")
        self.gridLayout.addWidget(self.radioButton_8, 0, 0, 1, 1)
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout.addWidget(self.radioButton_5, 1, 0, 1, 1)
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_6.setObjectName("radioButton_6")
        self.gridLayout.addWidget(self.radioButton_6, 2, 0, 1, 1)
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_7.setObjectName("radioButton_7")
        self.gridLayout.addWidget(self.radioButton_7, 3, 0, 1, 1)
        self.radioButton_9 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_9.setObjectName("radioButton_9")
        self.gridLayout.addWidget(self.radioButton_9, 4, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout_5.addWidget(self.groupBox_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_2.addWidget(self.lineEdit_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_5.addWidget(self.lineEdit_8)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_5.addWidget(self.lineEdit_9)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_4.addWidget(self.lineEdit_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_4.addWidget(self.lineEdit_7)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.plotButton = QtWidgets.QPushButton(self.centralwidget)
        self.plotButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.plotButton.setObjectName("plotButton")
        self.verticalLayout_6.addWidget(self.plotButton)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.gridLayout_5.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_10 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_10.setObjectName("radioButton_10")
        self.horizontalLayout.addWidget(self.radioButton_10)
        self.radioButton_11 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_11.setObjectName("radioButton_11")
        self.horizontalLayout.addWidget(self.radioButton_11)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.gridLayout_5.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 590, 26))
        self.menubar.setAutoFillBackground(False)
        self.menubar.setStyleSheet("color: rgb(255, 255, 255);")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setAutoFillBackground(False)
        self.menuFile.setStyleSheet("")
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("color: rgb(255, 255, 255);")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionHelp)
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chooseButton.setText(_translate("MainWindow", "Choose"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.groupBox.setTitle(_translate("MainWindow", "Choose Color Of Markers"))
        self.radioButton.setText(_translate("MainWindow", "Blue"))
        self.radioButton_2.setText(_translate("MainWindow", "Red"))
        self.radioButton_3.setText(_translate("MainWindow", "Yellow"))
        self.radioButton_4.setText(_translate("MainWindow", "White"))
        self.maskButton.setText(_translate("MainWindow", "Masked Video"))
        self.trackButton.setText(_translate("MainWindow", "Tracked Marker"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Choose Coordinates"))
        self.radioButton_8.setText(_translate("MainWindow", "X / Frames"))
        self.radioButton_5.setText(_translate("MainWindow", "Y / Frames"))
        self.radioButton_6.setText(_translate("MainWindow", "Z / Frames"))
        self.radioButton_7.setText(_translate("MainWindow", "X / Y"))
        self.radioButton_9.setText(_translate("MainWindow", "X / Y / Z "))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Choose ROI</p><p>Frontal View</p></body></html>"))
        self.lineEdit_4.setText(_translate("MainWindow", "X Start point "))
        self.lineEdit_3.setText(_translate("MainWindow", "Height"))
        self.lineEdit_5.setText(_translate("MainWindow", "Y Start Point "))
        self.lineEdit_2.setText(_translate("MainWindow", "Width"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Choose ROI</p><p>Profile View</p></body></html>"))
        self.lineEdit_8.setText(_translate("MainWindow", "X Start point "))
        self.lineEdit_9.setText(_translate("MainWindow", "Height"))
        self.lineEdit_6.setText(_translate("MainWindow", "Y Start Point "))
        self.lineEdit_7.setText(_translate("MainWindow", "Width"))
        self.plotButton.setText(_translate("MainWindow", "Plot"))
        self.radioButton_10.setText(_translate("MainWindow", "CSV"))
        self.radioButton_11.setText(_translate("MainWindow", "TXT"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionClose.setText(_translate("MainWindow", "Close"))

import images
