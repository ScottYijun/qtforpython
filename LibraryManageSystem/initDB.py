""""
brief:pyqt5图片管理系统。
        数据库的初始化
date:2020-07-18
author:chenyijun
version: python V3.8.1 pyqt5 V5.14.0
"""
#https://blog.csdn.net/qiqiyingse/category_9285730.html
#https://blog.csdn.net/weixin_38312031/category_9274444.html

import os
import os.path
import sqlite3
import hashlib

# home = os.path.expanduser('~') #获取当前用户目录
# print(home) # C:\Users\username
# if '.BookManagerSystem' not in os.listdir(home):
#     os.mkdir(os.path.join(home, '.BookManagerSystem'))
#
# dbpath = os.path.join(home, '.BookManagerSystem', 'LibraryManagement.db')
# print(dbpath) # C:\Users\username\.BookManagerSystem\LibraryManagement.db

apath = os.path.abspath('.') #获取当前工作目录
print(apath)
if 'db' not in os.listdir(apath):
    os.mkdir(os.path.join(apath, 'db'))

dbpath = os.path.join(apath, 'db', 'LibraryManagement.db')
print(dbpath)

createUserTableString = """
CREATE TABLE IF NOT EXISTS user(
    userid CHAR(10) PRIMARY KEY,
    Name VARCHAR(20),
    Password CHAR(32),
    IsAdmin BIT,
    TimesBorrowed INT,
    NumBorrowed INT
)"""

createUser_BookTableString = """
CREATE TABLE IF NOT EXISTS User_Book(
    userid CHAR(10),
    BookID CHAR(6) PRIMARY KEY,
    BorrowTime DATE,
    ReturnTime DATE,
    BorrowState BIT
)"""

createBookTableString = """
CREATE TABLE IF NOT EXISTS Book(
    BookName VARCHAR(30),
    BookID CHAR(6),
    Auth VARCHAR(20),
    Category VARCHAR(20),
    Publisher VARCHAR(20),
    PublishTime DATE,
    NumStorage INT,
    NumCanBorrow INT,
    NumBorrowed INT
)"""

createAddOrDropBookTableString = """
CREATE TABLE IF NOT EXISTS AddOrDrop(
    BookID CHAR(6),
    ModifyTime DATE,
    AddOrDrop INT,
    Numbers INT
)"""


"""
数据库类，实现数据库的基本操作，创建，删除，切换库
"""
class DbManager(object):
    def __init__(self, *args):
        self.db = sqlite3.connect(*args)
        self.cursor = self.db.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, types, value, traceback):
        self.db.commit()
        return False

    def __del__(self):
        self.db.commit()
        self.db.close()

    def switchDb(self, *args):
        self.db.close()
        self.db = sqlite3.connect(*args)
        self.cursor = self.db.cursor()

    def createTable(self, tableString):
        self.cursor.execute(tableString)
        self.db.commit()

    def commitAndClose(self):
        self.db.commit()
        self.db.close()

"""
用户类，实现初始化数据，添加普通用户，添加管理员，查询用户信息，查询管理员，更新密码，借书还书
"""
class UserDbManager(DbManager):
    def __init__(self, database=dbpath, *args):
        super().__init__(database, *args)
        self.initDb()

    def initDb(self):
        self.createTable(createUserTableString)

    def initDatabase(self):
        password = 'admin123'
        hl = hashlib.md5()  #
        hl.update(password.encode(encoding = 'utf-8'))
        md5password = hl.hexdigest()
        self.addAdminUser('admin', 'scott', md5password)

        password = 'user123'
        hl = hashlib.md5()  #
        hl.update(password.encode(encoding = 'utf-8'))
        md5password = hl.hexdigest()
        self.addUser('user000000', 'user000000', md5password)

    def addUser(self, userid, Name, Password, IsAdmin = 0):
        """添加普通用户"""
        insertData = self.cursor.execute("""INSERT INTO user
                    (userid, Name, Password, IsAdmin, TimesBorrowed, NumBorrowed) VALUES 
                    ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')
                    """.format(userid, Name, Password, IsAdmin, 0, 0))
        self.db.commit()

    def addAdminUser(self, userid, Name, Password):
        """添加管理员用户"""
        self.addUser(userid, Name, Password, IsAdmin = 1)

    def querybyUserid(self, userid):
        fetchedData = self.cursor.execute("SELECT * FROM user WHERE userid = '%s'" % (userid))
        byUserid = fetchedData.fetchall()#通过fetchall接受全部数据，是一个list,list的每个元素是tuple类型数据
        print(byUserid)
        #return fetchedData.fetchall()
        return byUserid

    def getAdmineUserInfo(self):
        """获取管理员用户"""
        fetchedData = self.cursor.execute("SELECT userid, Name FROM user WHERE IsAdmin = 1")
        adminUser = fetchedData.fetchall()  # 通过fetchall接受全部数据，是一个list,list的每个元素是tuple类型数据
        print(adminUser)
        return fetchedData

    def getUserinfo(self):
        """获取一般用户"""
        fetchedData = self.cursor.execute("SELECT userid, Name FROM user WHERE IsAdmin = 0")
        normalUser = fetchedData.fetchall()  # 通过fetchall接受全部数据，是一个list,list的每个元素是tuple类型数据
        print(normalUser)
        return fetchedData

    def updatePassword(self, password, userid):
        fetchedData = self.cursor.execute("UPDATE User SET Password = '%s' WHERE userid = %s" % (password, userid))
        self.db.commit()

    def borrowOrReturnBook(self, userid, borrow = 1):
        if borrow == 1:
            fetchedData = self.cursor.execute("UPDATE User SET TimesBorrowed = TimesBorrowed + 1, NumBorrowed = NumBorrowed + 1 WHERE userid = '%s'" % userid)
        else:
            fetchedData = self.cursor.execute("UPDATE User SET TimesBorrowed = TimesBorrowed - 1, NumBorrowed = NumBorrowed - 1 WHERE userid = '%s'" % userid)
        self.db.commit()

"""
图书类，书库初駋化，添加图书，删除图书，借书，不书，收籍查询等
"""
class BookDbManager(DbManager):
    def __init__(self, database = dbpath, *args):
        super().__init__(database, *args)
        self.initDb()

    def initDb(self):
        self.createTable(createBookTableString)

    def initDatabase(self):
        self.addBOOK('力学', 'IS1000', '刘斌', '教育', '中国科学技术大学 ', '1999-01-01', 100, 100, 0)
        self.addBOOK('微积分', 'IS1001', '牛顿莱布尼兹', '教育', '中国科学技术大学', '1998-01-01', 14, 14, 0)
        self.addBOOK('电磁场论', 'IS1002', '叶邦角', '教育', '中国科学技术大学', '1997-01-01', 24, 24, 0)
        self.addBOOK('热学', 'IS1003', '张鹏飞', '教育', '中国科学技术大学', '2002-01-01', 45, 45, 0)
        self.addBOOK('电动力学', 'IS1004', '叶邦角', '教育', '中国科学技术大学', '2003-01-01', 100, 100, 0)
        self.addBOOK('数据库', 'IS1006', '袁平波', '教育', '中国科学技术大学', '2010-01-01', 10, 10, 0)
        self.addBOOK('电磁学', 'IS1005', '叶邦角', '教育', '中国科学技术大学 ', '2012-01-01', 43, 43, 0)
        self.addBOOK('数学分析', 'IS1007', '陈卿', '教育', '中国科学技术大学', '2013-01-01', 23, 23, 0)
        self.addBOOK('吉米多维奇题解1', 'IS1008', '吉米多维奇', '教育', '俄罗斯出版社', '2010-01-01', 50, 50, 0)
        self.addBOOK('吉米多维奇题解2', 'IS1009', '吉米多维奇', '教育', '俄罗斯出版社', '2010-01-01', 50, 50, 0)
        self.addBOOK('吉米多维奇题解3', 'IS1010', '吉米多维奇', '教育', '俄罗斯出版社', '2010-01-01', 50, 50, 0)
        self.addBOOK('吉米多维奇题解4', 'IS1011', '吉米多维奇', '教育', '俄罗斯出版社', '2010-01-01', 50, 50, 0)
        self.addBOOK('吉米多维奇题解5', 'IS1012', '吉米多维奇', '教育', '俄罗斯出版社', '2010-01-01', 50, 50, 0)
        self.addBOOK('吉米多维奇题解6', 'IS1013', '吉米多维奇', '教育', '俄罗斯出版社', '2010-01-01', 50, 50, 0)
        self.addBOOK('朗道力学', 'IS1014', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0)
        self.addBOOK('朗道电动力学', 'IS1015', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0)
        self.addBOOK('朗道量子力学', 'IS1016', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0)
        self.addBOOK('朗道量子电动力学', 'IS1017', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0)
        self.addBOOK('朗道统计物理学', 'IS1018', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0)
        self.addBOOK('朗道流体力学', 'IS1019', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0)
        self.addBOOK('朗道弹性理论力学', 'IS1020', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0)
        self.addBOOK('朗道物理动力学', 'IS1021', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0)
        self.addBOOK('植物学', 'IS1022', '佚名', '生物学', '高等教育出版社', '2011-05-01', 50, 50, 0)
        self.addBOOK('动物学', 'IS1023', '佚名', '生物学', '高等教育出版社', '2011-05-01', 50, 50, 0)
        self.addBOOK('细胞生物学', 'IS1024', '佚名', '生物学', '高等教育出版社', '2011-05-01', 50, 50, 0)
        self.addBOOK('动物生理学', 'IS1025', '佚名', '生物学', '高等教育出版社', '2011-05-01', 50, 50, 0)
        self.addBOOK('古生物学', 'IS1026', '佚名', '生物学', '高等教育出版社', '2011-05-01', 100, 100, 0)
        self.addBOOK('高等数学', 'IS1027', '佚名', '教育', '高等教育出版社', '2011-05-01', 50, 50, 0)
        self.addBOOK('线性代数', 'IS1029', '佚名', '教育', '高等教育出版社', '2011-05-01', 50, 50, 0)
        self.addBOOK('C++程序设计', 'IS1030', '孙广中', '教育', '中国科学技术大学', '2011-05-01', 50, 50, 0)
        self.addBOOK('C程序设计', 'IS1031', '郑重', '教育', '中国科学技术大学', '2011-05-01', 50, 50, 0)
        self.addBOOK('数据结构', 'IS1032', '顾为兵', '教育', '中国科学技术大学', '2011-05-01', 50, 50, 0)
        self.addBOOK('信号与系统', 'IS1033', '李卫平', '教育', '中国科学技术大学', '2011-05-01', 50, 50, 0)
        self.addBOOK('线性电子线路', 'IS1034', '陆伟', '教育', '中国科学技术大学', '2011-05-01', 50, 50, 0)

    def addBOOK(self, BookName, BookID, Auth, Category, Publisher, PublishTime, NumStorage, NumCanBorrow, NumBorrowed):
        """添加书籍"""
        insertData = self.cursor.execute("""INSERT INTO Book
                    (BookName, BookID, Auth, Category, Publisher, publishTime, NumStorage, NumCanBorrow, NumBorrowed) VALUES
                    ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}')
                    """.format(BookName, BookID, Auth, Category, Publisher, PublishTime, NumStorage, NumCanBorrow, NumBorrowed))
        self.db.commit()

    def dropBook(self, bookId):
        insertData = self.cursor.execute("DELETE FROM Book WHERE BookID = '%s'" % (bookId))
        self.db.commit()

    def updateBookinfo(self, addBookNum, bookId, addFlag = 1):
        if addFlag == 1:
            self.cursor.execute("UPDATE Book SET NumStorage = NumStorage+%d, NumCanBorrow = NumCanBorrow+%d WHERE BookID = '%s'"
                                %(addBookNum, addBookNum, bookId))
        else:
            self.cursor.execute("UPDATE Book SET NumStorage = NumStorage-%d, NumCanBorrow = NumCanBorrow - %d WHERE BookID = '%s'"
                                %(addBookNum, addBookNum, bookId))
        self.db.commit()

    def getBookinfo(self):
        """获得所有书籍"""
        fetchedData = self.cursor.execute("SELECT * FROM Book")
        return fetchedData.fetchall()

    def querybyBookID(self, BookID):
        fetchedData = self.cursor.execute("SELECT * FROM Book WHERE BookID = '%s'" % (BookID))
        return fetchedData.fetchall()

    def queryBookByKeywords(self, keywords):
        fetchedData = self.cursor.execute("SELECT * FROM Book ORDER BY %s limit %s, %s" % (keywords, 0, 5))
        return fetchedData.fetchall()

    def borrowOrReturnBook(self, BookID, borrowflag = 1):
        if borrowflag == 1:
            fetchedData = self.cursor.execute("UPDATE Book SET NumCanBorrow = NumCanBorrow - 1, NumBorrowed = NumBorrowed + 1 WHERE BookID = '%s'" % BookID)
        else:
            fetchedData = self.cursor.execute("UPDATE Book SET NumCanBorrow = NumCanBorrow + 1, NumBorrowed = NumBorrowed - 1 WHERE BookID = '%s'" % BookID)
        self.db.commit()

"""
添加删除类
"""
class AddOrDropManager(DbManager):
    def __init__(self, database = dbpath, *args):
        super().__init__(database, *args)
        self.initDb()

    def initDb(self):
        self.createTable(createAddOrDropBookTableString)

    def initDatabase(self):
        self.insertValue('IS1000', '2018-04-22', 1, 100)
        self.insertValue('IS1001', '2018-04-22', 1, 14)
        self.insertValue('IS1002', '2018-04-22', 1, 24)
        self.insertValue('IS1003', '2018-04-22', 1, 45)
        self.insertValue('IS1004', '2018-04-22', 1, 100)
        self.insertValue('IS1004', '2018-04-27', 1, 45)
        self.insertValue('IS1005', '2018-04-27', 1, 45)
        self.insertValue('IS1006', '2018-04-28', 1, 10)
        self.insertValue('IS1007', '2018-04-28', 1, 23)
        self.insertValue('IS1008', '2018-04-28', 1, 50)
        self.insertValue('IS1009', '2018-04-28', 1, 50)
        self.insertValue('IS1010', '2018-04-28', 1, 50)
        self.insertValue('IS1011', '2018-04-28', 1, 50)
        self.insertValue('IS1012', '2018-04-28', 1, 50)
        self.insertValue('IS1013', '2018-04-28', 1, 50)
        self.insertValue('IS1014', '2018-04-28', 1, 50)
        self.insertValue('IS1015', '2018-04-28', 1, 50)
        self.insertValue('IS1016', '2018-04-28', 1, 50)
        self.insertValue('IS1017', '2018-04-28', 1, 50)
        self.insertValue('IS1018', '2018-04-28', 1, 50)
        self.insertValue('IS1019', '2018-04-28', 1, 50)
        self.insertValue('IS1020', '2018-04-28', 1, 50)
        self.insertValue('IS1021', '2018-04-28', 1, 50)
        self.insertValue('IS1022', '2018-04-28', 1, 50)
        self.insertValue('IS1023', '2018-04-28', 1, 50)
        self.insertValue('IS1024', '2018-04-28', 1, 50)
        self.insertValue('IS1025', '2018-04-28', 1, 50)
        self.insertValue('IS1026', '2018-04-28', 1, 100)
        self.insertValue('IS1027', '2018-04-28', 1, 50)
        self.insertValue('IS1029', '2018-04-28', 1, 50)
        self.insertValue('IS1030', '2018-04-28', 1, 50)
        self.insertValue('IS1031', '2018-04-28', 1, 50)
        self.insertValue('IS1032', '2018-04-28', 1, 50)
        self.insertValue('IS1033', '2018-04-28', 1, 50)
        self.insertValue('IS1034', '2018-04-28', 1, 50)

    def insertValue(self, BookID, time, AddorDrop, addBookNum):
        insertData = self.cursor.execute("INSERT INTO AddOrDrop VALUES ('%s', '%s', %d, %d)" % (BookID, time, AddorDrop, addBookNum))
        self.db.commit()

    def addinfo(self, BookID, time, addBookNum):
        self.insertValue(BookID, time, 1, addBookNum)

    def dropinfo(self, BookID, time, addBookNum):
        self.insertValue(BookID, time, 0, addBookNum)

    def getAllinfo(self):
        """获得所有书籍"""
        fetchedData = self.cursor.execute("SELECT * from AddOrDrop")
        return fetchedData.fetchall()

def testuserdb():
    userDb = UserDbManager()
    userDb.addAdminUser('admin', 'admin', '123456')
    userDb.addAdminUser('administrator', 'admin1', '123456')
    userDb.addUser('Test', 'AAA', '123456')
    userDb.addUser('Test1', 'BBB', '123456')
    userDb.addUser('Test2', 'CCC', '123456')
    userDb.getAdmineUserInfo()
    userDb.getUserinfo()
    userDb.querybyUserid('admins')
    userDb.querybyUserid('admin')

def testAddDropBookData():
    userDb = AddOrDropManager()

    allbook = userDb.getAllinfo()
    for book in allbook:
        print(book)
        # print(" ".join('%s' % ids for ids in a))
        # a=list(book)
        # print(a)

def testBookDB():
    userDb = BookDbManager()
    if len(userDb.querybyBookID('IS1006')):
        print("书籍已经存在，更新数量")
        userDb.updateBookinfo(10, 'IS1005')
    else:
        print("书籍不存在，直接插入")
        userDb.addBOOK('力学3',   'IS1006'  ,'刘斌3',  '教育',  '中国科学技术大学', '1999-01-01',  '34' , '34' , '1')
    allbook = userDb.getBookinfo()

    print('all book length = %d' % len(allbook))
    for book in allbook:
        print(book)

    print("按照bookid查询")
    bookid = userDb.querybyBookID('IS1006')
    if len(bookid):
        print(bookid)
    print("按照auth排序查询前几页")
    keybook = userDb.queryBookByKeywords('Auth')
    print(keybook)

if __name__ == '__main__':
    print("test start()====================")
    testuserdb()
    print("testuserdb()====================")
    testAddDropBookData()
    print("testAddDropBookData()====================")
    testBookDB()
    print("testBookDB()====================")










