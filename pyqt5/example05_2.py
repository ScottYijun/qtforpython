""""
brief:QColorDialog
QColorDialog显示一个用于选择颜色值的对话框。
date:2020-01-26
author:chenyijun
"""

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame,
                             QColorDialog, QApplication)
from PyQt5.QtGui import QColor

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0)
        self.btn = QPushButton("Dialog", self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget{background-color: %s}" % col.name())
        self.frm.setGeometry(130, 22, 100, 100)
        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle("Color Dialog")
        self.show()

    def showDialog(self):
        print("self==========", self)
        col = QColorDialog.getColor()
        print("col==========", col)
        if col.isValid():
            self.frm.setStyleSheet("QWidget{background-color:%s}" % col.name())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
