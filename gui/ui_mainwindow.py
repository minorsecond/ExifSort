# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/rwardrup/Projects/ExifSort/gui/ui_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(632, 365)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.inputPathEdit = QtWidgets.QLineEdit(self.frame)
        self.inputPathEdit.setObjectName("inputPathEdit")
        self.gridLayout_2.addWidget(self.inputPathEdit, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)
        self.rootPathLabel = QtWidgets.QLabel(self.frame)
        self.rootPathLabel.setObjectName("rootPathLabel")
        self.gridLayout_2.addWidget(self.rootPathLabel, 1, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_2.addWidget(self.checkBox_4, 2, 1, 1, 1)
        self.outputPathEdit = QtWidgets.QLineEdit(self.frame)
        self.outputPathEdit.setObjectName("outputPathEdit")
        self.gridLayout_2.addWidget(self.outputPathEdit, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_3.addWidget(self.checkBox_2, 2, 1, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_3.addWidget(self.checkBox_3, 0, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_3.addWidget(self.checkBox, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)
        self.filenameFormatLineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.filenameFormatLineEdit.setObjectName("filenameFormatLineEdit")
        self.gridLayout_4.addWidget(self.filenameFormatLineEdit, 1, 2, 1, 1)
        self.attributeSelectorInput = QtWidgets.QComboBox(self.frame_3)
        self.attributeSelectorInput.setObjectName("attributeSelectorInput")
        self.gridLayout_4.addWidget(self.attributeSelectorInput, 2, 2, 1, 1)
        self.filenameFormatLabel = QtWidgets.QLabel(self.frame_3)
        self.filenameFormatLabel.setObjectName("filenameFormatLabel")
        self.gridLayout_4.addWidget(self.filenameFormatLabel, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 12, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 1)
        self.mainButtonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.mainButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.mainButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.mainButtonBox.setObjectName("mainButtonBox")
        self.gridLayout.addWidget(self.mainButtonBox, 5, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 632, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ExifSort"))
        self.label.setText(_translate("MainWindow", "Output Path:"))
        self.rootPathLabel.setText(_translate("MainWindow", "Input Path:"))
        self.checkBox_4.setText(_translate("MainWindow", "Separate output path"))
        self.checkBox_2.setText(_translate("MainWindow", "Tiff"))
        self.checkBox_3.setText(_translate("MainWindow", "JPG"))
        self.checkBox.setText(_translate("MainWindow", "RAW"))
        self.label_3.setText(_translate("MainWindow", "Attribute Selector"))
        self.filenameFormatLabel.setText(_translate("MainWindow", "FIlename Format:"))
