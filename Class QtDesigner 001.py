# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Example_QtDesigner_001.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_000(object):
    def setupUi(self, MainWindow_000):
        MainWindow_000.setObjectName("MainWindow_000")
        MainWindow_000.resize(800, 744)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow_000.sizePolicy().hasHeightForWidth())
        MainWindow_000.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow_000)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 250, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 250, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 250, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(30, 40, 291, 192))
        self.listView.setObjectName("listView")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(570, 690, 193, 28))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 311, 221))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(340, 70, 141, 301))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 260, 93, 28))
        self.pushButton_4.setToolTip("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 50, 121, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(10, 70, 111, 20))
        self.checkBox.setObjectName("checkBox")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox.setGeometry(QtCore.QRect(30, 230, 91, 22))
        self.spinBox.setObjectName("spinBox")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 170, 121, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 150, 121, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton.setGeometry(QtCore.QRect(10, 130, 121, 20))
        self.radioButton.setObjectName("radioButton")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(30, 100, 101, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(30, 20, 101, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(30, 200, 101, 20))
        self.label_9.setObjectName("label_9")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(350, 30, 121, 22))
        self.comboBox.setObjectName("comboBox")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(490, 30, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(643, 30, 141, 281))
        self.textEdit.setObjectName("textEdit")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(650, 340, 131, 321))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 10, 101, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(500, 10, 91, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(660, 10, 121, 20))
        self.label_4.setObjectName("label_4")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 300, 261, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 340, 291, 371))
        self.listWidget.setObjectName("listWidget")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(670, 320, 111, 20))
        self.label_6.setObjectName("label_6")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(490, 70, 141, 301))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 260, 93, 28))
        self.pushButton_5.setToolTip("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 50, 121, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_4.setEnabled(False)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 70, 111, 20))
        self.checkBox_4.setObjectName("checkBox_4")
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_2.setGeometry(QtCore.QRect(30, 230, 91, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 170, 121, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_5.setEnabled(False)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 150, 121, 20))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_6.setEnabled(False)
        self.radioButton_6.setGeometry(QtCore.QRect(10, 130, 121, 20))
        self.radioButton_6.setObjectName("radioButton_6")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(30, 100, 101, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(30, 20, 101, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(30, 200, 101, 20))
        self.label_12.setObjectName("label_12")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(490, 380, 141, 301))
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 260, 93, 28))
        self.pushButton_6.setToolTip("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_5.setGeometry(QtCore.QRect(10, 50, 121, 20))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_6.setEnabled(False)
        self.checkBox_6.setGeometry(QtCore.QRect(10, 70, 111, 20))
        self.checkBox_6.setObjectName("checkBox_6")
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_3.setGeometry(QtCore.QRect(30, 230, 91, 22))
        self.spinBox_3.setObjectName("spinBox_3")
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_7.setEnabled(False)
        self.radioButton_7.setGeometry(QtCore.QRect(10, 170, 121, 20))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_8.setGeometry(QtCore.QRect(10, 150, 121, 20))
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_9 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_9.setGeometry(QtCore.QRect(10, 130, 121, 20))
        self.radioButton_9.setObjectName("radioButton_9")
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        self.label_13.setGeometry(QtCore.QRect(30, 100, 101, 20))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(30, 20, 101, 20))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label_15.setGeometry(QtCore.QRect(30, 200, 101, 20))
        self.label_15.setObjectName("label_15")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(340, 380, 141, 301))
        self.groupBox_5.setObjectName("groupBox_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_7.setGeometry(QtCore.QRect(30, 260, 93, 28))
        self.pushButton_7.setToolTip("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox_7.setGeometry(QtCore.QRect(10, 50, 121, 20))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox_8.setGeometry(QtCore.QRect(10, 70, 111, 20))
        self.checkBox_8.setObjectName("checkBox_8")
        self.spinBox_4 = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinBox_4.setGeometry(QtCore.QRect(30, 230, 91, 22))
        self.spinBox_4.setObjectName("spinBox_4")
        self.radioButton_10 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_10.setGeometry(QtCore.QRect(10, 170, 121, 20))
        self.radioButton_10.setObjectName("radioButton_10")
        self.radioButton_11 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_11.setGeometry(QtCore.QRect(10, 150, 121, 20))
        self.radioButton_11.setObjectName("radioButton_11")
        self.radioButton_12 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_12.setGeometry(QtCore.QRect(10, 130, 121, 20))
        self.radioButton_12.setObjectName("radioButton_12")
        self.label_16 = QtWidgets.QLabel(self.groupBox_5)
        self.label_16.setGeometry(QtCore.QRect(30, 100, 101, 20))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox_5)
        self.label_17.setGeometry(QtCore.QRect(30, 20, 101, 20))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_5)
        self.label_18.setGeometry(QtCore.QRect(30, 200, 101, 20))
        self.label_18.setObjectName("label_18")
        self.listWidget.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.listView.raise_()
        self.buttonBox.raise_()
        self.comboBox.raise_()
        self.lineEdit.raise_()
        self.textEdit.raise_()
        self.plainTextEdit.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.progressBar.raise_()
        self.label_6.raise_()
        self.groupBox_3.raise_()
        self.groupBox_4.raise_()
        self.groupBox_5.raise_()
        MainWindow_000.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_000)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow_000.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_000)
        self.statusbar.setObjectName("statusbar")
        MainWindow_000.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_000)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_000)

    def retranslateUi(self, MainWindow_000):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_000.setWindowTitle(_translate("MainWindow_000", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow_000", "Button_000"))
        self.pushButton_2.setText(_translate("MainWindow_000", "Button_001"))
        self.pushButton_3.setText(_translate("MainWindow_000", "Button_002"))
        self.groupBox.setTitle(_translate("MainWindow_000", "GroupBox"))
        self.groupBox_2.setTitle(_translate("MainWindow_000", "GroupBox_000"))
        self.pushButton_4.setText(_translate("MainWindow_000", "Button_003"))
        self.checkBox_2.setText(_translate("MainWindow_000", "CheckBox_000"))
        self.checkBox.setText(_translate("MainWindow_000", "CheckBox_001"))
        self.radioButton_3.setText(_translate("MainWindow_000", "RadioButton_002"))
        self.radioButton_2.setText(_translate("MainWindow_000", "RadioButton_001"))
        self.radioButton.setText(_translate("MainWindow_000", "RadioButton_000"))
        self.label_7.setText(_translate("MainWindow_000", "TextLabel_001"))
        self.label_8.setText(_translate("MainWindow_000", "TextLabel_000"))
        self.label_9.setText(_translate("MainWindow_000", "TextLabel_002"))
        self.label_2.setText(_translate("MainWindow_000", "TextLabel_000"))
        self.label_3.setText(_translate("MainWindow_000", "TextLabel_001"))
        self.label_4.setText(_translate("MainWindow_000", "TextLabel_004"))
        self.label_6.setText(_translate("MainWindow_000", "TextLabel_005"))
        self.groupBox_3.setTitle(_translate("MainWindow_000", "GroupBox_001"))
        self.pushButton_5.setText(_translate("MainWindow_000", "Button_003"))
        self.checkBox_3.setText(_translate("MainWindow_000", "CheckBox_000"))
        self.checkBox_4.setText(_translate("MainWindow_000", "CheckBox_001"))
        self.radioButton_4.setText(_translate("MainWindow_000", "RadioButton_002"))
        self.radioButton_5.setText(_translate("MainWindow_000", "RadioButton_001"))
        self.radioButton_6.setText(_translate("MainWindow_000", "RadioButton_000"))
        self.label_10.setText(_translate("MainWindow_000", "TextLabel_001"))
        self.label_11.setText(_translate("MainWindow_000", "TextLabel_000"))
        self.label_12.setText(_translate("MainWindow_000", "TextLabel_002"))
        self.groupBox_4.setTitle(_translate("MainWindow_000", "GroupBox_003"))
        self.pushButton_6.setText(_translate("MainWindow_000", "Button_003"))
        self.checkBox_5.setText(_translate("MainWindow_000", "CheckBox_000"))
        self.checkBox_6.setText(_translate("MainWindow_000", "CheckBox_001"))
        self.radioButton_7.setText(_translate("MainWindow_000", "RadioButton_002"))
        self.radioButton_8.setText(_translate("MainWindow_000", "RadioButton_001"))
        self.radioButton_9.setText(_translate("MainWindow_000", "RadioButton_000"))
        self.label_13.setText(_translate("MainWindow_000", "TextLabel_001"))
        self.label_14.setText(_translate("MainWindow_000", "TextLabel_000"))
        self.label_15.setText(_translate("MainWindow_000", "TextLabel_002"))
        self.groupBox_5.setTitle(_translate("MainWindow_000", "GroupBox_002"))
        self.pushButton_7.setText(_translate("MainWindow_000", "Button_003"))
        self.checkBox_7.setText(_translate("MainWindow_000", "CheckBox_000"))
        self.checkBox_8.setText(_translate("MainWindow_000", "CheckBox_001"))
        self.radioButton_10.setText(_translate("MainWindow_000", "RadioButton_002"))
        self.radioButton_11.setText(_translate("MainWindow_000", "RadioButton_001"))
        self.radioButton_12.setText(_translate("MainWindow_000", "RadioButton_000"))
        self.label_16.setText(_translate("MainWindow_000", "TextLabel_001"))
        self.label_17.setText(_translate("MainWindow_000", "TextLabel_000"))
        self.label_18.setText(_translate("MainWindow_000", "TextLabel_002"))
