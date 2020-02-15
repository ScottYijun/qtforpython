""""
brief:滑动条 QSlider
QSlider是一个带有简单滑块的控件。滑块可以前后拖动。我们可以通过拖动选择一个特定的值。
有时使用滑动条比直接输入数字或使用旋转框更加自然。
在下面的例子中，我们会显示一个滑动条与一个标签，标签用于显示图片，并通过滑动条控件图片的显示 。
注意这里图片只能用ico格式的，png格式图片会显示不了。
date:2020-01-26
author:chenyijun
"""
import sys
from PyQt5.QtWidgets import QWidget, QSlider, QLabel, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        slider = QSlider(Qt.Horizontal, self)
        slider.setFocusPolicy(Qt.NoFocus)
        slider.setGeometry(30, 40, 100, 30)
        slider.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("qt5.ico"))
        self.label.setGeometry(160, 40, 80, 30)
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle("QSlider")
        self.show()

    def changeValue(self, value):
        if value == 0:
            self.label.setPixmap(QPixmap("pen.ico"))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap("pen.ico"))
        elif value > 30 and value < 80:
            self.label.setPixmap(QPixmap("sensor.ico"))
        else:
            self.label.setPixmap(QPixmap("sideshow.ico"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

