""""
brief:使用BeautifulSoup和request爬天堂网的图片
author:chenyijun
date:2020-02-15
"""

import requests
from bs4 import BeautifulSoup
import re
import urllib
import urllib.request


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
            x = 0
            for img in page.find_all('img'): #文件夹的url
                #print(img)
                imgurl = img.get('src') #获取src字段
                save_path = "F:/github/qtforpython/spider/tiantang/" + str(i) + "_" + str(x) + ".jpg" #拼接图片保存路径
                imghttp = 'https:' + imgurl #拼按图片的url路径
                #print(imghttp)
                urllib.request.urlretrieve(imghttp, save_path, cbk)
                x += 1

if __name__ == '__main__':
    spidertupian()

#html格式化文档网站
#https://tool.oschina.net/codeformat/

#参考文档
# https://blog.csdn.net/qq_27492735/article/details/78478750
#
# https://www.cnblogs.com/Deaseyy/p/11266742.html
# https://blog.csdn.net/nicholas_K/article/details/85275793
# https://blog.csdn.net/dayun555/article/details/79375841
# https://www.52pojie.cn/thread-1071469-1-1.html
# https://www.cnblogs.com/fwc1994/p/5878934.html