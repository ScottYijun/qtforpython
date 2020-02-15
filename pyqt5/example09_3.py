""""
brief:颜色
颜色是一个对象代表红、绿、蓝(RGB)强度值。有效的RGB值的范围从0到255。
我们可以用不同的方法定义了一个颜色。最常见的是RGB十进制或十六进制值的值。
我们也可以使用一个RGBA值代表红色,绿色,蓝色,透明度。
我们添加一些额外的信息透明度。透明度值255定义了完全不透明,0是完全透明的,
例如颜色是无形的。
date:2020-01-26
author:chenyijun
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 100)
        self.setWindowTitle("Colours")
        self.show()

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)
        self.drawRectangles(painter)
        painter.end()

    def drawRectangles(self, painter):
        col = QColor(0, 0, 0)
        col.setNamedColor("#d4ded4")
        painter.setPen(col)

        painter.setBrush(QColor(200, 0, 0))
        painter.drawRect(10, 15, 90, 60)
        painter.setBrush(QColor(255, 80, 0, 160))
        painter.drawRect(130, 15, 90, 60)
        painter.setBrush(QColor(25, 0, 90, 200))
        painter.drawRect(250, 15, 90, 60)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

