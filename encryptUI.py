# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'encryptUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RSA(object):
    def setupUi(self, RSA):
        RSA.setObjectName("RSA")
        RSA.setWindowModality(QtCore.Qt.NonModal)
        RSA.resize(378, 417)
        RSA.setWindowOpacity(1.0)
        RSA.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(RSA)
        self.centralwidget.setObjectName("centralwidget")
        self.eKeyText = QtWidgets.QLabel(self.centralwidget)
        self.eKeyText.setGeometry(QtCore.QRect(70, 80, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.eKeyText.setFont(font)
        self.eKeyText.setObjectName("eKeyText")
        self.nKeyText = QtWidgets.QLabel(self.centralwidget)
        self.nKeyText.setGeometry(QtCore.QRect(20, 130, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nKeyText.setFont(font)
        self.nKeyText.setObjectName("nKeyText")
        self.EncryptedText = QtWidgets.QLabel(self.centralwidget)
        self.EncryptedText.setGeometry(QtCore.QRect(130, 250, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EncryptedText.setFont(font)
        self.EncryptedText.setObjectName("EncryptedText")
        self.BlockText = QtWidgets.QLabel(self.centralwidget)
        self.BlockText.setGeometry(QtCore.QRect(70, 30, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BlockText.setFont(font)
        self.BlockText.setObjectName("BlockText")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 292, 171, 73))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.result = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.result.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.result.setFont(font)
        self.result.setAcceptDrops(False)
        self.result.setTabChangesFocus(True)
        self.result.setReadOnly(True)
        self.result.setAcceptRichText(True)
        self.result.setObjectName("result")
        self.verticalLayout.addWidget(self.result)
        self.blockLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.blockLineEdit.setGeometry(QtCore.QRect(130, 40, 131, 31))
        self.blockLineEdit.setObjectName("blockLineEdit")
        self.eKeyLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.eKeyLineEdit.setGeometry(QtCore.QRect(130, 90, 131, 31))
        self.eKeyLineEdit.setObjectName("eKeyLineEdit")
        self.nKeyLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nKeyLineEdit.setGeometry(QtCore.QRect(130, 140, 131, 31))
        self.nKeyLineEdit.setObjectName("nKeyLineEdit")
        self.encryptButton = QtWidgets.QPushButton(self.centralwidget)
        self.encryptButton.setGeometry(QtCore.QRect(130, 200, 121, 51))
        self.encryptButton.setObjectName("encryptButton")
        RSA.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RSA)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 378, 21))
        self.menubar.setObjectName("menubar")
        self.menuEncrypt = QtWidgets.QMenu(self.menubar)
        self.menuEncrypt.setObjectName("menuEncrypt")
        RSA.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RSA)
        self.statusbar.setObjectName("statusbar")
        RSA.setStatusBar(self.statusbar)
        self.actionEncrypt = QtWidgets.QAction(RSA)
        self.actionEncrypt.setObjectName("actionEncrypt")
        self.actionDecrypt = QtWidgets.QAction(RSA)
        self.actionDecrypt.setObjectName("actionDecrypt")
        self.actionClose = QtWidgets.QAction(RSA)
        self.actionClose.setObjectName("actionClose")
        self.menuEncrypt.addAction(self.actionEncrypt)
        self.menuEncrypt.addSeparator()
        self.menuEncrypt.addSeparator()
        self.menuEncrypt.addAction(self.actionClose)
        self.menubar.addAction(self.menuEncrypt.menuAction())

        self.retranslateUi(RSA)
        QtCore.QMetaObject.connectSlotsByName(RSA)

    def retranslateUi(self, RSA):
        _translate = QtCore.QCoreApplication.translate
        RSA.setWindowTitle(_translate("RSA", "RSA Encrypter"))
        self.eKeyText.setText(_translate("RSA", "e Key"))
        self.nKeyText.setText(_translate("RSA", "n Key (or p*q)"))
        self.EncryptedText.setText(_translate("RSA", "Encrypted block"))
        self.BlockText.setText(_translate("RSA", "Block"))
        self.encryptButton.setText(_translate("RSA", "Encrypt"))
        self.menuEncrypt.setTitle(_translate("RSA", "Preferences"))
        self.actionEncrypt.setText(_translate("RSA", "Encrypt"))
        self.actionDecrypt.setText(_translate("RSA", "Decrypt"))
        self.actionClose.setText(_translate("RSA", "Close"))