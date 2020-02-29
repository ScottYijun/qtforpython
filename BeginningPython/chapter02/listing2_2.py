#从类似于http://www.something.com的URL中提取域名

url = input('Please enter the URL: ')
domain = url[11:-4]
print("Domain name: " + domain)