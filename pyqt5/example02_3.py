""""
brief:表格布局 QGridLayout
表格布局将空间划分为行和列。我们使用QGridLayout类创建一个网格布局。
author:chenyijun
date:2020-01-26
"""
import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        names = ["Cls", "Bck", "", "Close",
                 "7", "8", "9", "/",
                 "4", "5", "6", "*",
                 "1", "2", "3", "-",
                 "0", ".", "=", "+"]
        positions = [(i, j) for i in range(5) for j in range(4)]
        for position, name in zip(positions, names):
            if name == "":
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(350, 150)
        self.setWindowTitle("Calculator")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example();
    sys.exit(app.exec_())


