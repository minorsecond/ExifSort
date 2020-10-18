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
        MainWindow.resize(855, 398)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pathFormatLabel = QtWidgets.QLabel(self.frame_3)
        self.pathFormatLabel.setObjectName("pathFormatLabel")
        self.gridLayout_4.addWidget(self.pathFormatLabel, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)
        self.pathFormatLineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.pathFormatLineEdit.setObjectName("pathFormatLineEdit")
        self.gridLayout_4.addWidget(self.pathFormatLineEdit, 1, 2, 1, 1)
        self.whiteSpaceReplacementSelector = QtWidgets.QComboBox(self.frame_3)
        self.whiteSpaceReplacementSelector.setObjectName("whiteSpaceReplacementSelector")
        self.gridLayout_4.addWidget(self.whiteSpaceReplacementSelector, 3, 2, 1, 1)
        self.attributeSelectorInput = QtWidgets.QComboBox(self.frame_3)
        self.attributeSelectorInput.setObjectName("attributeSelectorInput")
        self.gridLayout_4.addWidget(self.attributeSelectorInput, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.frame_3, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.outputPathEdit = QtWidgets.QLineEdit(self.frame)
        self.outputPathEdit.setObjectName("outputPathEdit")
        self.gridLayout_2.addWidget(self.outputPathEdit, 3, 1, 1, 1)
        self.rootPathLabel = QtWidgets.QLabel(self.frame)
        self.rootPathLabel.setObjectName("rootPathLabel")
        self.gridLayout_2.addWidget(self.rootPathLabel, 1, 0, 1, 1)
        self.seperateOutputPathCheckbox = QtWidgets.QCheckBox(self.frame)
        self.seperateOutputPathCheckbox.setObjectName("seperateOutputPathCheckbox")
        self.gridLayout_2.addWidget(self.seperateOutputPathCheckbox, 2, 1, 1, 1)
        self.inputPathEdit = QtWidgets.QLineEdit(self.frame)
        self.inputPathEdit.setObjectName("inputPathEdit")
        self.gridLayout_2.addWidget(self.inputPathEdit, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)
        self.inputPathBrowseButton = QtWidgets.QPushButton(self.frame)
        self.inputPathBrowseButton.setObjectName("inputPathBrowseButton")
        self.gridLayout_2.addWidget(self.inputPathBrowseButton, 1, 2, 1, 1)
        self.outputPathBrowseButton = QtWidgets.QPushButton(self.frame)
        self.outputPathBrowseButton.setObjectName("outputPathBrowseButton")
        self.gridLayout_2.addWidget(self.outputPathBrowseButton, 3, 2, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tiffCheckBox = QtWidgets.QCheckBox(self.frame_2)
        self.tiffCheckBox.setObjectName("tiffCheckBox")
        self.gridLayout_3.addWidget(self.tiffCheckBox, 2, 1, 1, 1)
        self.jpgCheckBox = QtWidgets.QCheckBox(self.frame_2)
        self.jpgCheckBox.setObjectName("jpgCheckBox")
        self.gridLayout_3.addWidget(self.jpgCheckBox, 0, 1, 1, 1)
        self.rawCheckBox = QtWidgets.QCheckBox(self.frame_2)
        self.rawCheckBox.setObjectName("rawCheckBox")
        self.gridLayout_3.addWidget(self.rawCheckBox, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 8, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 7, 0, 1, 1)
        self.mainButtonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.mainButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.mainButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.mainButtonBox.setObjectName("mainButtonBox")
        self.gridLayout.addWidget(self.mainButtonBox, 9, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 855, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ExifSort"))
        self.pathFormatLabel.setText(_translate("MainWindow", "Path Format:"))
        self.label_2.setText(_translate("MainWindow", "Replace Whitespace with:"))
        self.label_3.setText(_translate("MainWindow", "Attribute Selector"))
        self.rootPathLabel.setText(_translate("MainWindow", "Input Path:"))
        self.seperateOutputPathCheckbox.setText(_translate("MainWindow", "Separate output path"))
        self.label.setText(_translate("MainWindow", "Output Path:"))
        self.inputPathBrowseButton.setText(_translate("MainWindow", "Browse"))
        self.outputPathBrowseButton.setText(_translate("MainWindow", "Browse"))
        self.tiffCheckBox.setText(_translate("MainWindow", "Tiff"))
        self.jpgCheckBox.setText(_translate("MainWindow", "JPG"))
        self.rawCheckBox.setText(_translate("MainWindow", "RAW"))

