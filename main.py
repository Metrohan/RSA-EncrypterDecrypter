from PyQt5.QtWidgets import QApplication, QDesktopWidget
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
import sys
import string

import decryptRSA
import decryptUI
import encryptUI
import encryptRSA
import separateWord
import separateBlocks


class MyGUI(QtWidgets.QMainWindow, encryptUI.Ui_RSA):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.show()
        self.setFixedSize(400, 400)

        self.encryptButton.clicked.connect(self.button_click)
        self.actionDecryptE.triggered.connect(self.switch_to_decrypt_ui)

    def block(self):
        word_ = self.blockLineEdit.text()
        block1, block2 = separateWord.separate1(word_)
        return block1, block2

    def eKey(self):
        eKey_ = self.eKeyLineEdit.text()
        return eKey_

    def nKey(self):
        nKey_ = self.nKeyLineEdit.text()
        return nKey_

    def button_click(self):
        try:
            _block, _block2 = self.block()
            _eKey = int(self.eKey())
            _nKey = int(self.nKey())
            if _eKey > _nKey:
                self.result.setText("e Key cannot greater than n Key!")

            else:
                result_ = encryptRSA.encrypt(_block, _block2, _eKey, _nKey)
                self.result.setFont(QFont('Arial', 14))
                self.result.setText(str(result_))
        except ValueError:
            self.result.setFont(QFont('Arial', 10))
            self.result.setText("Please check your values. You must enter a word and two numeric keys.")
        except Exception as e:
            self.result.setText(str(e))

    def switch_to_decrypt_ui(self):
        global decrypt_widget
        decrypt_widget = MyGUI2()
        self.hide()
        decrypt_widget.show()


class MyGUI2(QtWidgets.QMainWindow, decryptUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.show()
        self.setupUi(self)
        self.setFixedSize(400, 400)

        self.pushButton.clicked.connect(self.button_click2)
        self.actionEncyrptD.triggered.connect(self.switch_to_encrypt_ui)

    def block(self):
        block_ = self.encLineEdit.text()
        block1, block2 = separateBlocks.separate(block_)
        return block1, block2

    def p(self):
        p_ = self.pLineEdit.text()
        return p_

    def q(self):
        q_ = self.qLineEdit.text()
        return q_

    def eKey(self):
        eKey_ = self.eKeyLineEdit.text()
        return eKey_

    def button_click2(self):
        try:
            _block, _block2 = self.block()
            _p = int(self.p())
            _q = int(self.q())
            _nKey = _p * _q
            _invModNum = ((_p - 1) * (_q - 1))
            _eKey = int(self.eKey())
            _d = pow(_eKey, -1, _invModNum)
            result_ = decryptRSA.decrypt(_block, _block2, _d, _nKey)
            self.textEdit.setFont(QFont('Arial', 14))
            self.textEdit.setText(str(result_))

        except ValueError:
            self.textEdit.setFont(QFont('Arial', 10))
            self.textEdit.setText("Please check your values. You must enter a word, two integers and a numeric key.")
        except Exception as e:
            self.textEdit.setText(str(e))

    def switch_to_encrypt_ui(self):
        global encrypt_widget
        encrypt_widget = MyGUI()
        self.hide()
        encrypt_widget.show()


def main():
    app = QApplication(sys.argv)
    main_widget = MyGUI()
    main_widget.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
