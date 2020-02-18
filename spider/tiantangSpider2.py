""""
brief:使用BeautifulSoup和request爬天堂网的图片
下载的图片以原名下载到对应的目录下
author:chenyijun
date:2020-02-16
"""

import requests
from bs4 import BeautifulSoup
import re
import urllib
import urllib.request
import os

#创建目录
#1、os.path.exists(path) 判断一个目录是否存在
#2、os.makedirs(path) 多层创建目录
#3、os.mkdir(path) 创建目录

def pmkdir(dir):
    dir = dir.strip() #去除首位空格
    dir = dir.rstrip("\\") #去除尾部\符号
    #判断路径是否存， 存在 True  不存在  False
    isExists = os.path.exists(dir)

    #判断结果
    if not isExists:
        #如果不存在则创建目录
        os.makedirs(dir)
        #print(dir + "创建成功")
        return True;
    else:
        #如果目录存在则不创建，并提示目录存在
        #print(dir + "目录存在")
        return False

def cbk(a, b, c):
    '''''回调函数
    @a:已经下载的数据块
    @b:数据块的大小
    @c:远程文件的大小
    '''
    per=100.0*a*b/c
    if per>100:
        per=100
    print ('%.2f%%' % per)
    print(" ")

url = 'https://www.ivsky.com/tupian/meishishijie/'  #取一个图片目录  美食世界
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12513.400','Referer':'http://www.ivsky.com/tupian/qita/index_11.html'}
html = requests.get(url, headers = headers) #获取网页内容
#print(html) #太多了，打印不出来

soup = BeautifulSoup(html.text,'html.parser')

def spidertupian():
    print(os.getcwd()) #获取当前工作目录路径
    print(os.path.abspath('.')) #获取当前工作目录路径
    print(os.path.abspath('..')) #获取当前工作的父目录 ！注意是父目录路径
    print(os.path.abspath(os.curdir)) #获取当前工作目录路径
    for i in range(1, 12):
        link = url +'/index_'+str(i)+'.html'
        #print(link) #打印链接

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12513.400',
            'Referer':'http://www.ivsky.com/tupian/qita/index_11.html'}
        html = requests.get(link, headers=headers)
        mess = BeautifulSoup(html.text, 'html.parser')
        # 查找标签为'ul', class属性为'ali'的标签元素，因为class是python的关键字，所以这里需要加个下划线'_'
        for page in mess.find_all('ul', class_='ali'):
            #print(page) #打印带<ul class="ali">标签的
            #print("---------------------------")
            for img in page.find_all('img'): #文件夹的url
                #print(img)
                imgurl = img.get('src') #获取src字段_
                image_name = imgurl.split('/')[-1] #获取图片名
                save_dir = os.getcwd() + "/tiantang/titlepage" + str(i) #每一页对应一个目录
                isExists = os.path.exists(save_dir) #判断目录是否存在

                if not isExists:
                    pmkdir(save_dir)  # 目录不存在，创建目录

                save_path = save_dir + "/" + image_name #拼接图片保存路径
                imghttp = 'https:' + imgurl #拼按图片的url路径
                print(imghttp)
                print(save_path)
                urllib.request.urlretrieve(imghttp, save_path, cbk) #封面图下载

if __name__ == '__main__':
    spidertupian()


#html格式化文档网站
#https://tool.oschina.net/codeformat/

#参考文档
# https://blog.csdn.net/qq_27492735/article/details/78478750
#
# https://www.cnblogs.com/monsteryang/p/6574550.html
# https://www.cnblogs.com/Jomini/p/8636129.html
# https://blog.csdn.net/weixin_44517681/article/details/102820832