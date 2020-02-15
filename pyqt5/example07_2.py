""""
brief:文本框 QLineEdit
QLineEdit是用于输入或编辑单行文本的控件。它还有撤销重做、剪切复制和拖拽功能。
date:2020-01-26
author:chenyijun
"""

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        lineEdit = QLineEdit(self)
        self.label.move(60, 40)
        lineEdit.textChanged[str].connect(self.onChanged)
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle("QLineEdit")
        self.show()

    def onChanged(self, text):
        self.label.setText(text)
        self.label.adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


