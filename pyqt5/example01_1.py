""""
fileName:simple.py
brief:一个PyQt5的简单的例子
author:chenyijun
date:2020-01-25
"""
import sys

#这里我们提供必要的引用，基本控件位于PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    #每一PyQt5应用程序必须创建一个应用程序对象。sys.arg 参数是一个列表，从命令行输入参数。
    app = QApplication(sys.argv)
    #QWidget部件是PyQt5所有用户界面对象的基类。他为QWidget提供默认构造函灵敏，默认构造函数没有父类。
    w = QWidget();
    #resize()方法调整窗口的大小，这窗口是250px宽，150px高
    w.resize(350, 300);
    #move()方法移动口在屏幕上的位置到x = 300, y = 300坐标.
    w.move(300, 300);
    #设置窗口的标题
    w.setWindowTitle("Simple")
    #显示在屏上
    w.show();
    #系统exit()方法确保存应用程序于净的退出的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
    sys.exit(app.exec_())
