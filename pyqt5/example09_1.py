""""
brief:绘制文本
我们先以窗体内Unicode文本的绘制为例。
date:2020-01-26
author:chenyijun
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.text = u'\u041b\u0435\u0432 \u041d\u0438\u043a\u043e\u043b\u0430\
\u0435\u0432\u0438\u0447 \u0422\u043e\u043b\u0441\u0442\u043e\u0439: \n\
\u0410\u043d\u043d\u0430 \u041a\u0430\u0440\u0435\u043d\u0438\u043d\u0430'
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle("Draw text")
        self.show()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.drawText(event, painter)
        painter.end()

    def drawText(self, event, painter):
        painter.setPen(QColor(168, 34, 3))
        painter.setFont(QFont("Decorative", 10))
        painter.drawText(event.rect(), Qt.AlignCenter, self.text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
