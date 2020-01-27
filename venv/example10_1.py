""""
brief:PyQt5自定义控件
PyQt5包含种类丰富的控件。但能满足所有需求的控件库是不存在的。
通常控件库只提供了像按钮、文本控件、滑块等最常用的控件。
但如果需要某种特殊的控件，我们只能自己动手来实现。 自定义控件需要使用工具库提供的绘图工具，
可能有两种方式：在已有的控件上进行拓展或从头开始创建自定义控件。
Burning widget(烧录控件)
这个控件可能会在Nero，K3B或其他CD/DVD烧录软件中见到。
author:chenyijun
date:2020-01-27
"""

import sys
from PyQt5.QtWidgets import (QWidget, QSlider, QApplication,
                             QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import QObject, Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QFont, QColor, QPen

class Communicate(QObject):
    updateBW = pyqtSignal(int)

class BurningWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setMinimumSize(1, 30)
        self.value = 75
        self.num = [75, 150, 225, 300, 375, 450, 525, 600, 675]

    def setValue(self, value):
        self.value = value

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)
        self.drawWidget(painter)
        painter.end()

    def drawWidget(self, painter):
        font = QFont("Serif", 7, QFont.Light)
        painter.setFont(font)
        size = self.size()
        w = size.width()
        h = size.height()
        step = int(round(w / 10.0))

        till = int(((w / 750.0) * self.value))
        full = int(((w / 750.0) * 700))

        if self.value >= 700:
            painter.setPen(QColor(255, 255, 255))
            painter.setBrush(QColor(255, 255, 184))
            painter.drawRect(0, 0, full, h)
            painter.setPen(QColor(255, 175, 175))
            painter.setBrush(QColor(255, 175, 175))
            painter.drawRect(full, 0, till - full, h)
        else:
            painter.setPen(QColor(255, 255, 255))
            painter.setBrush(QColor(255, 255, 184))
            painter.drawRect(0, 0, till, h)

        pen = QPen(QColor(20, 20, 20), 1, Qt.SolidLine)
        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)
        painter.drawRect(0, 0, w - 1, h -1)
        j = 0;
        for i in range(step, 10 * step, step):
            painter.drawLine(i, 0, i, 5)
            metrics = painter.fontMetrics()
            fw = metrics.width(str(self.num[j]))
            painter.drawText(i - fw / 2, h / 2, str(self.num[j]))
            j = j + 1

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        slider = QSlider(Qt.Horizontal, self)
        slider.setFocusPolicy(Qt.NoFocus)
        slider.setRange(1, 750)
        slider.setValue(75)
        slider.setGeometry(30, 40, 150, 30)

        self.c = Communicate()
        self.wid = BurningWidget()
        self.c.updateBW[int].connect(self.wid.setValue)

        slider.valueChanged[int].connect(self.changeValue)
        hbox = QHBoxLayout()
        hbox.addWidget(self.wid)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 390, 210)
        self.setWindowTitle("Burning Widget")
        self.show()

    def changeValue(self, value):
        self.c.updateBW.emit(value)
        self.wid.repaint()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())




