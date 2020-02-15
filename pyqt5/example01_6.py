""""
brief:窗口显示在屏幕的中间
默认情况下,如果我们单击x按钮窗口就关门了。有时我们想修改这个默认的行为。
例如我们在编辑器中修改了一个文件,当关闭他的时候，我们显示一个消息框确认。
author:chenyijun
date:2020-01-25
"""
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(350, 150)
        self.center()
        self.setWindowTitle("Center")
        self.show()

    #控制窗口显示在屏幕中心的方法
    def center(self):
        #获得窗口
        qr = self.frameGeometry()
        #获是屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        #显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv);
    ex = Example()
    sys.exit(app.exec_())

