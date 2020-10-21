""""
brief:修改密码
date:2020-10-06
author:chenyijun
version: python V3.8.1 pyqt5 V5.14.0
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qdarkstyle
from initDB import UserDbManager
import hashlib



class changePasswordDialog(QDialog):
    def __init__(self, parent=None):
        super(changePasswordDialog, self).__init__(parent)

        # 设置该窗口为一个当以层次的模态窗口，阻塞它的父窗口、祖父窗口和各个兄弟窗口接受输入信息，此时能够在弹出来的对话框中接收输入法信息。
        self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle("修改密码")
        self.setUpUI()
        self.userdb = UserDbManager()

    def setUpUI(self):
        self.resize(300, 280)
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        self.titlelabel = QLabel(" 修改密码")
        self.userIDLabel = QLabel("账    号：")
        # self.studentNameLabel=QLabel("姓    名：")
        self.oldPasswordLabel = QLabel("旧 密 码：")
        self.passwordLabel = QLabel("新 密 码：")
        self.confirmPasswordLabel = QLabel("确认密码：")

        self.userIDEdit = QLineEdit()
        # self.studentNameEdit=QLineEdit()
        self.oldPasswordEdit = QLineEdit()
        self.passwordEdit = QLineEdit()
        self.confirmPasswordEdit = QLineEdit()

        self.changePasswordButton = QPushButton("确认修改")
        self.changePasswordButton.setFixedWidth(140)
        self.changePasswordButton.setFixedHeight(32)

        self.layout.addRow("", self.titlelabel)
        self.layout.addRow(self.userIDLabel, self.userIDEdit)
        # self.layout.addRow(self.studentNameLabel,self.studentNameEdit)
        self.layout.addRow(self.oldPasswordLabel, self.oldPasswordEdit)
        self.layout.addRow(self.passwordLabel, self.passwordEdit)
        self.layout.addRow(self.confirmPasswordLabel, self.confirmPasswordEdit)
        self.layout.addRow("", self.changePasswordButton)

        font = QFont()
        font.setPixelSize(20)
        self.titlelabel.setFont(font)

        font.setPixelSize(16)
        self.userIDLabel.setFont(font)
        self.userIDEdit.setFont(font)
        # self.studentNameLabel.setFont(font)
        # self.studentNameEdit.setFont(font)
        self.oldPasswordLabel.setFont(font)
        self.oldPasswordEdit.setFont(font)
        self.passwordLabel.setFont(font)
        self.passwordEdit.setFont(font)
        self.confirmPasswordLabel.setFont(font)
        self.confirmPasswordEdit.setFont(font)
        self.changePasswordButton.setFont(font)

        self.titlelabel.setMargin(8)  # 控件与窗体的左右边距为8
        self.layout.setVerticalSpacing(10)  # 控件与控件的边距为8，Layout拥有得属性

        # 设置长度
        self.userIDEdit.setMaxLength(10)
        self.oldPasswordEdit.setMaxLength(16)
        self.passwordEdit.setMaxLength(16)
        self.confirmPasswordEdit.setMaxLength(16)
        # 设置密码掩膜
        # QLineEdit.Password输入字符后就立马显示为星号
        # QLineEdit.PasswordEchoOnEdit为输入时为字符，失去焦点为星号

        ##self.oldPasswordEdit.setEchoMode(QLineEdit.Password)
        ##self.passwordEdit.setEchoMode(QLineEdit.Password)
        ##self.confirmPasswordEdit.setEchoMode(QLineEdit.Password)

        self.oldPasswordEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.passwordEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.confirmPasswordEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        # 设置校验
        reg = QRegExp("PB[0~9]{8}")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg)
        self.userIDEdit.setValidator(pValidator)

        reg = QRegExp("[a-zA-z0-9]+$")
        pValidator.setRegExp(reg)
        self.oldPasswordEdit.setValidator(pValidator)
        self.passwordEdit.setValidator(pValidator)
        self.confirmPasswordEdit.setValidator(pValidator)

        # 设置信号与槽
        self.changePasswordButton.clicked.connect(self.changePasswordButtonClicked)

    def changePasswordButtonClicked(self):
        userID = self.userIDEdit.text()
        oldPassword = self.oldPasswordEdit.text()
        password = self.passwordEdit.text()
        confirmPassword = self.confirmPasswordEdit.text()
        if (userID == "" or oldPassword == "" or password == "" or confirmPassword == ""):
            print(QMessageBox.warning(self, "警告", "输入不可为空，请重新输入", QMessageBox.Yes, QMessageBox.Yes))
            return

        # 密码与确认密码不同
        if (password != confirmPassword):
            print(QMessageBox.warning(self, "警告", "两次输入密码不同,请确认输入", QMessageBox.Yes, QMessageBox.Yes))
            self.passwordEdit.clear()
            self.confirmPasswordEdit.clear()
            return

        userinfo = self.userdb.querybyUserid(userID)

        # 如果用户不存在
        if (not userinfo):
            print(QMessageBox.warning(self, "警告", "该用户不存在，请重新输入", QMessageBox.Yes, QMessageBox.Yes))
            self.userIDEdit.clear()
            return
            # 如果密码错误
        hl = hashlib.md5()
        hl.update(oldPassword.encode(encoding='utf-8'))
        md5password = hl.hexdigest()
        if (md5password != userinfo[0][2]):
            print(QMessageBox.warning(self, "警告", "原密码输入错误,请重新输入", QMessageBox.Yes, QMessageBox.Yes))
            self.oldPasswordEdit.clear()
            return

        # 修改密码
        hl = hashlib.md5()
        hl.update(password.encode(encoding='utf-8'))
        newmd5password = hl.hexdigest()

        self.userdb.updatePassword(newmd5password, userID)
        QMessageBox.information(self, "提醒", "修改密码成功，请登录系统!", QMessageBox.Yes, QMessageBox.Yes)
        self.close()
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(":/images/MainWindow_1.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = changePasswordDialog()
    mainMindow.show()
    sys.exit(app.exec_())
