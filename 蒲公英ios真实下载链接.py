# encoding:utf-8
# 2018/8/27
# Author:Scar丶殇痕

import requests, re
print('例子：https://www.pgyer.com/HAky，输入HAky就可以')
url = str(input("please input:"))
response = requests.get("https://www.pgyer.com/"+url)
print("https://www.pgyer.com/app/install/"+re.compile("aKey = '(.*?)'",re.S).findall(response.text)[0])
input()