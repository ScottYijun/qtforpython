""""
brief:对话框窗口或对话框是现代GUI应用程序最不可或缺的一部分。
一个对话框被定义为两个或两个以上的人之间的谈话。
在计算机应用程序对话框窗口用于“交谈”应用程序。
一个对话框用于输入数据,修改数据,更改应用程序设置等。
QInputDialog
QInputDialog提供了一种简单方便的对话框从用户得到一个值。
输入值可以是字符串,一个数字,或一个项目从一个列表。
date:2020-01-26
author:chenyijun
"""
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QInputDialog, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton("Dialog", self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        self.le = QLineEdit(self)
        self.le.move(130, 22)
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle("Input Dialog")
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, "Input Dialog",
                                        "Enter your name:")
        if ok:
            self.le.setText(str(text))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
