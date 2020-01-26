""""
brief:重新实现事件处理器
在PyQt5中常通过重新实现事件处理器来处理事件。
date:2020-01-26
author:chenyijun
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Event Handler")
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            print("esc press===============")
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


