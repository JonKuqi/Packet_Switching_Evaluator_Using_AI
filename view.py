# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1118, 905)
        MainWindow.setStyleSheet("background-color: #212121;")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 80, 291, 291))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("imgRouter.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 10, 901, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #ECECEC;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 440, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #ECECEC;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(440, 440, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #ECECEC;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(440, 540, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #ECECEC;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(440, 490, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #ECECEC;")
        self.label_6.setObjectName("label_6")
        self.btnGenerateProbability = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenerateProbability.setGeometry(QtCore.QRect(900, 440, 151, 31))
        self.btnGenerateProbability.setStyleSheet("color: #0D0D0D; border: none; font-size:14px; cursor: hand; border-radius: 15px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); background-color: #F9F9F9; ")
        self.btnGenerateProbability.setObjectName("btnGenerateProbability")
        self.txtGenerateProbability = QtWidgets.QLineEdit(self.centralwidget)
        self.txtGenerateProbability.setGeometry(QtCore.QRect(880, 490, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtGenerateProbability.setFont(font)
        self.txtGenerateProbability.setStyleSheet("color: #ECECEC;")
        self.txtGenerateProbability.setObjectName("txtGenerateProbability")
        self.txtTargetUsers = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTargetUsers.setGeometry(QtCore.QRect(710, 540, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtTargetUsers.setFont(font)
        self.txtTargetUsers.setStyleSheet("color: #ECECEC;")
        self.txtTargetUsers.setObjectName("txtTargetUsers")
        self.txtAllUsers = QtWidgets.QLineEdit(self.centralwidget)
        self.txtAllUsers.setGeometry(QtCore.QRect(220, 440, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtAllUsers.setFont(font)
        self.txtAllUsers.setStyleSheet("color: #ECECEC; border-width: 1px;")
        self.txtAllUsers.setObjectName("txtAllUsers")
        self.txtActivepPercentage = QtWidgets.QLineEdit(self.centralwidget)
        self.txtActivepPercentage.setGeometry(QtCore.QRect(680, 440, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtActivepPercentage.setFont(font)
        self.txtActivepPercentage.setStyleSheet("color: #ECECEC;")
        self.txtActivepPercentage.setObjectName("txtActivepPercentage")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 630, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: #ECECEC;")
        self.label_9.setObjectName("label_9")
        self.txtEnvironment = QtWidgets.QLineEdit(self.centralwidget)
        self.txtEnvironment.setGeometry(QtCore.QRect(20, 670, 691, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtEnvironment.setFont(font)
        self.txtEnvironment.setStyleSheet("color: #ECECEC;")
        self.txtEnvironment.setObjectName("txtEnvironment")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(710, 490, 111, 31))
        self.comboBox.setStyleSheet("color: #ECECEC; border-color: #ECECEC; border-width:2px;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 770, 411, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: #ECECEC;")
        self.label_10.setObjectName("label_10")
        self.txtResponse = QtWidgets.QLineEdit(self.centralwidget)
        self.txtResponse.setGeometry(QtCore.QRect(530, 760, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtResponse.setFont(font)
        self.txtResponse.setStyleSheet("color: #ECECEC;")
        self.txtResponse.setObjectName("txtResponse")
        self.btnGenerateResponse = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenerateResponse.setGeometry(QtCore.QRect(920, 670, 151, 31))
        self.btnGenerateResponse.setStyleSheet("color: #0D0D0D; border: none; font-size:14px; cursor: hand; border-radius: 15px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); background-color: #F9F9F9; ")
        self.btnGenerateResponse.setObjectName("btnGenerateResponse")
        self.comboLanguage = QtWidgets.QComboBox(self.centralwidget)
        self.comboLanguage.setGeometry(QtCore.QRect(740, 670, 151, 41))
        self.comboLanguage.setStyleSheet("color: #ECECEC; border-color: #ECECEC; border-width:2px;")
        self.comboLanguage.setObjectName("comboLanguage")
        self.comboLanguage.addItem("")
        self.comboLanguage.addItem("")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1080, 490, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #ECECEC;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(830, 440, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: #ECECEC;")
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 540, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: #ECECEC;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 490, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: #ECECEC;")
        self.label_12.setObjectName("label_12")
        self.txtBandwidth = QtWidgets.QLineEdit(self.centralwidget)
        self.txtBandwidth.setGeometry(QtCore.QRect(220, 490, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtBandwidth.setFont(font)
        self.txtBandwidth.setStyleSheet("color: #ECECEC;")
        self.txtBandwidth.setObjectName("txtBandwidth")
        self.txtBandwidthPerUser = QtWidgets.QLineEdit(self.centralwidget)
        self.txtBandwidthPerUser.setGeometry(QtCore.QRect(220, 540, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtBandwidthPerUser.setFont(font)
        self.txtBandwidthPerUser.setStyleSheet("color: #ECECEC;")
        self.txtBandwidthPerUser.setObjectName("txtBandwidthPerUser")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(370, 490, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: #ECECEC;")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(370, 540, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: #ECECEC;")
        self.label_14.setObjectName("label_14")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1118, 26))
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
        self.label_2.setText(_translate("MainWindow", "Packet Switching Probability Evaluator"))
        self.label_3.setText(_translate("MainWindow", "Number of all users:"))
        self.label_4.setText(_translate("MainWindow", "Active time percentage:"))
        self.label_5.setText(_translate("MainWindow", "Number of targeted users:"))
        self.label_6.setText(_translate("MainWindow", "Setting:"))
        self.btnGenerateProbability.setText(_translate("MainWindow", "Generate Probability"))
        self.label_9.setText(_translate("MainWindow", "Explain your placement area:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "More ( > )"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Equal ( = )"))
        self.comboBox.setItemText(2, _translate("MainWindow", "More or equal ( >= )"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Less ( < )"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Less or equal ( <= )"))
        self.label_10.setText(_translate("MainWindow", "Response:"))
        self.btnGenerateResponse.setText(_translate("MainWindow", "Generate Response"))
        self.comboLanguage.setItemText(0, _translate("MainWindow", "English"))
        self.comboLanguage.setItemText(1, _translate("MainWindow", "Albanian"))
        self.label_7.setText(_translate("MainWindow", "%"))
        self.label_8.setText(_translate("MainWindow", "%"))
        self.label_11.setText(_translate("MainWindow", "Bandwidht per user:"))
        self.label_12.setText(_translate("MainWindow", "Bandwidth: "))
        self.label_13.setText(_translate("MainWindow", "Gb/s"))
        self.label_14.setText(_translate("MainWindow", "Mb/s"))