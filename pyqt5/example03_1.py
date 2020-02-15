""""
brief:状态栏
状态栏用于显示状态信息。
author:chenyijun
date:2020-01-26
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage("Ready")
        self.setGeometry(300, 300, 250, 150)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())






