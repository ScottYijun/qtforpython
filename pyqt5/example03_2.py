""""
brief:菜单栏
菜单栏是常见的窗口应用程序的一部分。(Mac OS将菜单条不同。得到类似的结果,
我们可以添加以下行:menubar.setNativeMenuBar(假)。)
author:chenyijun
date:2020-01-26
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon("qt.png"), "&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit application")
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()
        # 创建一个菜单栏
        menubar = self.menuBar()
        # 创建一个菜单栏
        fileMenu = menubar.addMenu("&File")
        # 添加事件
        fileMenu.addAction(exitAction)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Simple menu")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
