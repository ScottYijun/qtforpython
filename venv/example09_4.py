""""
brief:QPen(画笔)
QPen是一个基本的图形对象。用于绘制线条、曲线和轮廓的矩形、椭圆、多边形或其他形状。
date:2020-01-26
author:chenyijun
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle("Pen Styles")
        self.show()

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)
        self.drawLines(painter)
        painter.end()

    def drawLines(self, painter):
        pen = QPen(Qt.black, 2, Qt.SolidLine)

        painter.setPen(pen)
        painter.drawLine(20, 40, 250, 40)

        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DashDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)
        painter.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 200, 250, 200)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        painter.setPen(pen)
        painter.drawLine(20, 240, 250, 240)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
