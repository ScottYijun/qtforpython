""""
brief:框布局 Boxlayout
我们使用QHBoxLayout和QVBoxLayout，来分别创建横向布局和纵向布局。
author:chenyijun
date:2020-01-26
"""
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout,
                             QApplication)
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 350, 150)
        self.setWindowTitle("Buttons")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example();
    sys.exit(app.exec_())








