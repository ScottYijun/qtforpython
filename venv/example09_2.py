""""
brief:画点
点是可以绘制的最简单的图形对象。
date:2020-01-26
author:chenyijun
"""

import sys, random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle("Points")
        self.show()

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)
        self.drawPoints(painter)
        painter.end()

    def drawPoints(self, painter):
        painter.setPen(Qt.red)
        size = self.size()
        for i in range(1000):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            painter.drawPoint(x, y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



