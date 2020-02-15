""""
brief:把他们放在一起
在本节的最后一个例子中,我们将创建一个菜单条,工具栏和状态栏的小窗口
author:chenyijun
date:2020-01-26
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)
        exitAction = QAction(QIcon("qt.png"), "Exit", self)
        exitAction.setShortcut("Ctrl + Q")
        exitAction.setStatusTip("Exit application")
        exitAction.triggered.connect(self.close)
        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle("Main Window")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
