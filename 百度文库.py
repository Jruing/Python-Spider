# encoding:utf-8
# 2018/11/12
import requests
import time
import re
fileid = "a698da9f9fc3d5bbfd0a79563c1ec5da50e2d6a7"
url = "https://wenku.baidu.com/api/doc/getdocinfo?callback=cb&doc_id={0}&t={1}&_={2}".format(fileid,int(time.time()*1000),int(time.time()*1000))
response = requests.get(url)
print(response.url)
print(response.text)
md5 = re.compile('"md5sum":"(.*?)"',re.S).findall(response.text)[0]
result_url = "https://wkretype.bdimg.com/retype/text/{0}{1}&callback=cb&pn=1&rn=4&type=txt&rsign=p_4-r_0-s_8780c&_={2}".format(fileid,md5,int(time.time()*1000))
response = requests.get(result_url)
print(response.url)
response.encoding = 'gbk'
print(response.text)