from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5 import QtWidgets, QtGui
import sys

import encryptUI
import encryptRSA


class MyGUI(QtWidgets.QMainWindow, encryptUI.Ui_RSA):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.actionClose.triggered.connect(self.shutDown)
        self.encryptButton.clicked.connect(self.button_click)

    def block(self):
        block_ = self.blockLineEdit.text()
        return block_

    def eKey(self):
        eKey_ = self.eKeyLineEdit.text()
        return eKey_

    def nKey(self):
        nKey_ = self.nKeyLineEdit.text()
        return nKey_

    def button_click(self):
        try:
            _block = int(self.block())
            _eKey = int(self.eKey())
            _nKey = int(self.nKey())
            if _eKey > _nKey:
                self.result.setText("e Key cannot greater than n Key!")
            else:
                result_ = encryptRSA.encrypt(_block, _eKey, _nKey)
                self.result.setText(str(result_))
        except ValueError:
            self.result.setText("Integers only!")

    def shutDown(self):
        exit()



if __name__ == "__main__":
    app = QApplication([])

    main_widget = MyGUI()

    main_widget.show()

    sys.exit(app.exec())
