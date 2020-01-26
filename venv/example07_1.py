""""
brief:QPixmap
QPixmap是用于处理图像的控件。是优化的显示图像在屏幕上。在我们的代码示例中,
我们将使用QPixmap窗口显示一个图像。
date:2020-01-26
author:chenyijun
"""

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("qt.png")
        label = QLabel(self)
        label.setPixmap(pixmap)
        hbox.addWidget(label)
        self.setLayout(hbox)
        self.move(300, 200)
        self.setWindowTitle("Red Rock")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

