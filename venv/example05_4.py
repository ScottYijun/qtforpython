""""
brief:QFileDialog
QFileDialog是一个让用户选择文件和目录的对话框，可用以选择打开或保存文件
date:2020-01-26
author:chenyijun
"""

import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog,
                             QApplication)
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon("qt.png"), "Open", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip("Open new File")
        openFile.triggered.connect(self.showDialog)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("File Dialog")
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "/home")
        if fname[0]:
            f = open(fname[0], "r")
            with f:
                data = f.read()
                self.textEdit.setText(data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

