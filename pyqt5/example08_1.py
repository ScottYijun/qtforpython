""""
brief:简单拖放
在第一个示例中,我们有一个QLineEdit QPushButton。
我们拖着纯文本的行编辑窗口小部件,然后放到按钮部件。按钮的标签会改变。
date:2020-01-26
author:chenyijun
"""

import sys
from PyQt5.QtWidgets import (QPushButton, QWidget, QLineEdit, QApplication)

class Button(QPushButton):
    def __init__(self, title, parent):
        print("__init__======title==", title)
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        print("dragEnterEvent========")
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        print("dropEvent========")
        self.setText(e.mimeData().text())

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        edit = QLineEdit("", self)
        edit.setMaximumSize(50, 30)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button("Button", self)
        button.setMaximumSize(100, 30)
        button.move(190, 65)

        self.setWindowTitle("Simple drag & drop")
        self.setGeometry(300, 300, 300, 150)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
