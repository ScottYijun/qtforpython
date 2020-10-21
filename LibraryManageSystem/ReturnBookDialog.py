""""
brief:还书功能
date:2020-10-05
author:chenyijun
version: python V3.8.1 pyqt5 V5.14.0
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qdarkstyle
import time
#from PyQt5.QtSql import *
from initDB import UserBookManager
from initDB import BookDbManager
from initDB import UserDbManager
#import images


class ReturnBookDialog(QDialog):
    return_book_success_signal = pyqtSignal()

    def __init__(self, userid, parent=None):
        super(ReturnBookDialog, self).__init__(parent)
        self.userid = userid
        self.setUpUI()
        # 设置该窗口为一个当以层次的模态窗口，阻塞它的父窗口、祖父窗口和各个兄弟窗口接受输入信息，此时能够在弹出来的对话框中接收输入法信息。
        self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle("归还书籍")
        self.userbookdb = UserBookManager()  # 借书记录
        self.bookdb = BookDbManager()  # 书籍管理
        self.userdb = UserDbManager()  # 用户管理

    def setUpUI(self):
        # 书名，书号，作者，分类，添加数量.出版社,出版日期
        # 书籍分类：哲学类、社会科学类、政治类、法律类、军事类、经济类、文化类、教育类、体育类、语言文字类、艺术类、历史类、地理类、天文学类、生物学类、医学卫生类、农业类
        BookCategory = ["哲学", "社会科学", "政治", "法律", "军事",
                        "经济", "文化", "教育", "体育", "语言文字",
                        "艺术", "历史", "地理", "天文学", "生物学",
                        "医学卫生", "农业"]
        self.resize(300, 400)
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        # Label控件
        self.returnStudentLabel = QLabel("还 书 人:")
        self.returnuseridLabel = QLabel(self.userid)
        self.titlelabel = QLabel("  归还书籍")
        self.bookNameLabel = QLabel("书    名:")
        self.BookIDLabel = QLabel("书    号:")
        self.authNameLabel = QLabel("作    者:")
        self.categoryLabel = QLabel("分    类:")
        self.publisherLabel = QLabel("出 版 社:")
        self.publishDateLabel = QLabel("出版日期:")

        # button控件
        self.returnBookButton = QPushButton("确认归还")

        # lineEdit控件
        self.bookNameEdit = QLineEdit()
        self.BookIDEdit = QLineEdit()
        self.authNameEdit = QLineEdit()
        self.categoryComboBox = QComboBox()  # 下拉菜单
        self.categoryComboBox.addItems(BookCategory)  # 向下拉菜单填充内容
        self.publisherEdit = QLineEdit()
        self.publishTime = QLineEdit()

        self.bookNameEdit.setMaxLength(10)
        self.BookIDEdit.setMaxLength(6)
        self.authNameEdit.setMaxLength(10)
        self.publisherEdit.setMaxLength(10)

        # 添加进formlayout
        self.layout.addRow("", self.titlelabel)
        self.layout.addRow(self.returnStudentLabel, self.returnuseridLabel)
        self.layout.addRow(self.bookNameLabel, self.bookNameEdit)
        self.layout.addRow(self.BookIDLabel, self.BookIDEdit)
        self.layout.addRow(self.authNameLabel, self.authNameEdit)
        self.layout.addRow(self.categoryLabel, self.categoryComboBox)
        self.layout.addRow(self.publisherLabel, self.publisherEdit)
        self.layout.addRow(self.publishDateLabel, self.publishTime)
        self.layout.addRow("", self.returnBookButton)

        # 设置字体
        font = QFont()
        font.setPixelSize(20)
        self.titlelabel.setFont(font)
        font.setPixelSize(16)
        self.returnuseridLabel.setFont(font)
        # font.setPixelSize(14)
        self.returnStudentLabel.setFont(font)
        self.bookNameLabel.setFont(font)
        self.BookIDLabel.setFont(font)
        self.authNameLabel.setFont(font)
        self.categoryLabel.setFont(font)
        self.publisherLabel.setFont(font)
        self.publishDateLabel.setFont(font)

        self.bookNameEdit.setFont(font)
        self.bookNameEdit.setReadOnly(True)  # 只读模式，不可输入内容
        self.bookNameEdit.setStyleSheet("background-color:#363636")  # 设置背景色 灰色

        self.BookIDEdit.setFont(font)

        self.authNameEdit.setFont(font)
        self.authNameEdit.setReadOnly(True)
        self.authNameEdit.setStyleSheet("background-color:#363636")

        self.publisherEdit.setFont(font)
        self.publisherEdit.setReadOnly(True)
        self.publisherEdit.setStyleSheet("background-color:#363636")

        self.publishTime.setFont(font)
        self.publishTime.setReadOnly(True)
        self.publishTime.setStyleSheet("background-color:#363636")

        self.categoryComboBox.setFont(font)  # QComboBox没有readonly属性
        self.categoryComboBox.setStyleSheet("background-color:#363636")

        # button设置
        font.setPixelSize(16)
        self.returnBookButton.setFont(font)
        self.returnBookButton.setFixedHeight(32)
        self.returnBookButton.setFixedWidth(140)

        # 设置间距
        self.titlelabel.setMargin(8)  # 距离窗体的间距
        self.layout.setVerticalSpacing(10)  # 控件之间的距离
        self.returnBookButton.clicked.connect(self.returnButtonClicked)
        self.BookIDEdit.textChanged.connect(self.BookIDEditChanged)  # 监控输入框
        # self.BookIDEdit.returnPressed.connect(self.BookIDEditChanged)

    def returnButtonClicked(self):
        # 获取书号，书号为空或并未借阅，则弹出错误
        # 更新Book_User表User表以及Book表
        BookID = self.BookIDEdit.text()
        # BookID为空的处理
        if (BookID == ""):
            print(QMessageBox.warning(self, "警告", "你所要还的书不存在，请查看输入", QMessageBox.Yes, QMessageBox.Yes))
            return

        # 如果未借阅
        borrowbook = self.userbookdb.borrowStatus(self.userid, BookID)
        if (not borrowbook[0][0]):
            print(QMessageBox.information(self, "提示", "您并未借阅此书，故无需归还", QMessageBox.Yes, QMessageBox.Yes))
            return

        # 更新User表
        self.userdb.borrowOrReturnBook(self.userid, borrow=0)

        # 更新Book表
        self.bookdb.borrowOrReturnBook(BookID, borrowflag=0)

        # 更新User_Book表
        timenow = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        self.userbookdb.borrowOrReturnBook(self.userid, BookID, timenow, borrowflag=0)

        print(QMessageBox.information(self, "提示", "归还成功!", QMessageBox.Yes, QMessageBox.Yes))
        self.return_book_success_signal.emit()
        self.close()
        return

    def BookIDEditChanged(self):
        BookID = self.BookIDEdit.text()
        if (BookID == ""):
            self.bookNameEdit.clear()
            self.publisherEdit.clear()
            self.authNameEdit.clear()
            self.publishTime.clear()

        # 在User_Book表中找借阅记录，如果存在借阅，则更新form内容
        borrowbook = self.userbookdb.borrowStatus(self.userid, BookID)
        if (borrowbook[0][0]):
            # 根据BookID查询书籍信息,更新form内容

            # 查询对应书号，如果存在就更新form
            bookinfo = self.bookdb.querybyBookID(BookID)
            if (bookinfo):
                self.bookNameEdit.setText(bookinfo[0][0])
                self.authNameEdit.setText(bookinfo[0][2])
                self.categoryComboBox.setCurrentText(bookinfo[0][3])
                self.publisherEdit.setText(bookinfo[0][4])
                self.publishTime.setText(bookinfo[0][5])
            return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(":/images/MainWindow_1.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = ReturnBookDialog("admin")
    mainMindow.show()
    sys.exit(app.exec_())