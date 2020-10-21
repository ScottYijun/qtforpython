""""
brief:添加书籍
date:2020-10-02
author:chenyijun
version: python V3.8.1 pyqt5 V5.14.0
"""


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qdarkstyle
import time

from initDB import BookDbManager
from initDB import AddOrDropManager
#from db.userInfoManager import BookDbManager
#from db.userInfoManager import AddOrDropManager
import images


class addBookDialog(QDialog):
    add_book_success_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(addBookDialog, self).__init__(parent)
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)
        self.bookdb = BookDbManager()
        self.addordropdb = AddOrDropManager()
        self.setWindowTitle("添加书籍")

    def setUpUI(self):
        # 书名，书号，作者，分类，添加数量.出版社,出版日期
        # 书籍分类：哲学类、社会科学类、政治类、法律类、军事类、经济类、文化类、教育类、体育类、语言文字类、艺术类、历史类、地理类、天文学类、生物学类、医学卫生类、农业类
        BookCategory = ["哲学", "社会科学", "政治", "法律", "军事", "经济", "文化", "教育", "体育", "语言文字", "艺术", "历史"
            , "地理", "天文学", "生物学", "医学卫生", "农业"]
        self.resize(300, 400)
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        # Label控件
        self.titlelabel = QLabel("  添加书籍")
        self.bookNameLabel = QLabel("书    名:")
        self.bookIdLabel = QLabel("书    号:")
        self.authNameLabel = QLabel("作    者:")
        self.categoryLabel = QLabel("分    类:")
        self.publisherLabel = QLabel("出 版 社:")
        self.publishDateLabel = QLabel("出版日期:")
        self.addNumLabel = QLabel("添加数量:")

        # button控件
        self.addBookButton = QPushButton("添 加")

        # lineEdit控件
        self.bookNameEdit = QLineEdit()
        self.bookIdEdit = QLineEdit()
        self.authNameEdit = QLineEdit()
        self.categoryComboBox = QComboBox()
        self.categoryComboBox.addItems(BookCategory)
        self.publisherEdit = QLineEdit()
        self.publishTime = QDateTimeEdit()
        self.publishTime.setDisplayFormat("yyyy-MM-dd")
        # self.publishDateEdit = QLineEdit()
        self.addNumEdit = QLineEdit()

        self.bookNameEdit.setMaxLength(10)
        self.bookIdEdit.setMaxLength(6)
        self.authNameEdit.setMaxLength(10)
        self.publisherEdit.setMaxLength(10)
        self.addNumEdit.setMaxLength(12)
        self.addNumEdit.setValidator(QIntValidator())

        # 添加进formlayout
        self.layout.addRow("", self.titlelabel)
        self.layout.addRow(self.bookNameLabel, self.bookNameEdit)
        self.layout.addRow(self.bookIdLabel, self.bookIdEdit)
        self.layout.addRow(self.authNameLabel, self.authNameEdit)
        self.layout.addRow(self.categoryLabel, self.categoryComboBox)
        self.layout.addRow(self.publisherLabel, self.publisherEdit)
        self.layout.addRow(self.publishDateLabel, self.publishTime)
        self.layout.addRow(self.addNumLabel, self.addNumEdit)
        self.layout.addRow("", self.addBookButton)

        # 设置字体
        font = QFont()
        font.setPixelSize(20)
        self.titlelabel.setFont(font)
        font.setPixelSize(14)
        self.bookNameLabel.setFont(font)
        self.bookIdLabel.setFont(font)
        self.authNameLabel.setFont(font)
        self.categoryLabel.setFont(font)
        self.publisherLabel.setFont(font)
        self.publishDateLabel.setFont(font)
        self.addNumLabel.setFont(font)

        self.bookNameEdit.setFont(font)
        self.bookIdEdit.setFont(font)
        self.authNameEdit.setFont(font)
        self.publisherEdit.setFont(font)
        self.publishTime.setFont(font)
        self.categoryComboBox.setFont(font)
        self.addNumEdit.setFont(font)

        # button设置
        font.setPixelSize(16)
        self.addBookButton.setFont(font)
        self.addBookButton.setFixedHeight(32)
        self.addBookButton.setFixedWidth(140)

        # 设置间距
        self.titlelabel.setMargin(8)
        self.layout.setVerticalSpacing(10)

        self.addBookButton.clicked.connect(self.addBookButtonCicked)

    def addBookButtonCicked(self):
        bookName = self.bookNameEdit.text()
        bookId = self.bookIdEdit.text()
        authName = self.authNameEdit.text()
        bookCategory = self.categoryComboBox.currentText()
        publisher = self.publisherEdit.text()
        publishTime = self.publishTime.text()
        addBookNum = self.addNumEdit.text()
        if (
                bookName == "" or bookId == "" or authName == "" or bookCategory == "" or publisher == "" or publishTime == "" or addBookNum == ""):
            print(QMessageBox.warning(self, "警告", "有字段为空，添加失败", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            addBookNum = int(addBookNum)
            bookinfo = self.bookdb.querybyBookID(bookId)

            if (bookinfo):
                self.bookdb.updateBookinfo(addBookNum, bookId, addFlag=1)
            else:
                self.bookdb.addBOOK(bookName, bookId, authName, bookCategory, publisher, publishTime, addBookNum,
                                    addBookNum, 0)

            # 插入droporinsert表
            timenow = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            self.addordropdb.addinfo(bookId, timenow, addBookNum)
            print(QMessageBox.information(self, "提示", "添加书籍成功!", QMessageBox.Yes, QMessageBox.Yes))
            self.add_book_success_signal.emit()
            self.close()
            self.clearEdit()
        return

    def clearEdit(self):
        self.bookNameEdit.clear()
        self.bookIdEdit.clear()
        self.authNameEdit.clear()
        self.addNumEdit.clear()
        self.publisherEdit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(":/images/MainWindow_1.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = addBookDialog()
    mainMindow.show()
    sys.exit(app.exec_())



