""""
fileName:messagebox.py
brief:消息框
默认情况下,如果我们单击x按钮窗口就关门了。有时我们想修改这个默认的行为。
例如我们在编辑器中修改了一个文件,当关闭他的时候，我们显示一个消息框确认。
author:chenyijun
date:2020-01-25
"""

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 150)
        self.setWindowTitle("Message box")
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Message",
            "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


"""
我们关闭窗口的时候,触发了QCloseEvent。我们需要重写closeEvent()事件处理程序。
reply = QMessageBox.question(self, 'Message',
    "Are you sure to quit?", QMessageBox.Yes | 
    QMessageBox.No, QMessageBox.No)

我们显示一个消息框,两个按钮:“是”和“不是”。
第一个字符串出现在titlebar。第二个字符串消息对话框中显示的文本。
第三个参数指定按钮的组合出现在对话框中。最后一个参数是默认按钮，这个是默认的按钮焦点。
if reply == QtGui.QMessageBox.Yes:
    event.accept()
else:
    event.ignore()  
我们处理返回值，如果单击Yes按钮,关闭小部件并终止应用程序。否则我们忽略关闭事件。
"""
