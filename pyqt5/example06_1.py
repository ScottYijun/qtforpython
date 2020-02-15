""""
brief:QQCheckBox
QCheckBox复选框控件，它有两个状态:打开和关闭，他是一个带有文本标签（Label）的控件。
复选框常用于表示程序中可以启用或禁用的功能。
date:2020-01-26
author:chenyijun
"""
import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        checkbox = QCheckBox("Show title", self)
        checkbox.move(20, 20)
        checkbox.toggle()
        checkbox.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("QCheckBox")
        self.show()

    def changeTitle(self, state):
        print("state-=========", state)
        if state == Qt.Checked:
            self.setWindowTitle("QCheckBox")
        else:
            self.setWindowTitle("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())