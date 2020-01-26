""""
brief:下拉列表 QComboBox
QComboBox是允许用户从下拉列表中进行选择的控件。
date:2020-01-26
author:chenyijun
"""

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QComboBox, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel("Ubuntu", self)
        combox = QComboBox(self)
        combox.addItem("Ubuntu")
        combox.addItem("Mandriva")
        combox.addItem("Fedora")
        combox.addItem("Arch")
        combox.addItem("Gentoo")
        combox.move(50, 50)

        combox.activated[str].connect(self.onActivated)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("QComboBox")
        self.show()

    def onActivated(self, text):
        self.label.setText(text)
        self.label.adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
