# encoding:utf-8
# 2018/7/6
# Author:Scar丶殇痕
import requests
import re
from fake_useragent import UserAgent
import time
import json,jsonpath
url = "https://qun.qq.com/cgi-bin/qun_mgr/get_group_list"
url1 = "https://qun.qq.com/cgi-bin/qun_mgr/get_friend_list"
header = {
    'useragent':UserAgent().chrome,
    'cookie':"自己手动获取"
}
skey = re.compile(" skey=(.*?);",re.S).findall(header['cookie'])[0]
def Get_Bkn(skey):
    # e = "@2eUVemMTP"
    e = "{0}".format(skey)
    t = 5381
    n = 0
    o = len(e)
    while n < o:
        t += (t << 5) + ord(e[n])
        n+=1
    t = 2147483647 & t
    print(t)
data = {
    'bkn': '{0}'.format(Get_Bkn(skey))
}
response = requests.post(url,headers=header,data=data)
responses = requests.post(url1,headers=header,data=data)
groups = json.loads(response.text)['join']
friends = json.loads(responses.text)['result']
# for i in groups:
#     print('群号:{0}  群名称：{1}   群主：{0}'.format(i['gc'],i['gn'],i['owner']))
# print(friends)
# info = re.compile("{'name': '(.*?)', 'uin': (.*?)}",re.S).findall(str(friends))
# for i,j in info:
#     print("备注：{0} 账号：{1}".format(i,j))
datas = {
    'gc': 435685112,
    'st': 0,
    'end': 1000,
    'sort': 0,
    'bkn': "自己手动获取"
}
headerss = {
    'useragent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.15 Safari/537.36',
    'cookie':"***"
}

qcy_url = "https://qun.qq.com/cgi-bin/qun_mgr/search_group_members"
qunchengy = requests.post(qcy_url,headers=headerss,data=datas)
menmbers = json.loads(qunchengy.text)
print(menmbers)
# 群名片
card = jsonpath.jsonpath(menmbers,'mems[*].card')
# 入群时间
join_time = jsonpath.jsonpath(menmbers,'mems[*].join_time')
# 最后发言时间
last_speak = jsonpath.jsonpath(menmbers,'mems[*].last_speak_time')
# 昵称
nick_name = jsonpath.jsonpath(menmbers,'mems[*].nick')
# q龄
qage = jsonpath.jsonpath(menmbers,'mems[*].qage')
# qq账号
account = jsonpath.jsonpath(menmbers,'mems[*].uin')
for c,n,a,q,j,l in zip(card,nick_name,account,qage,join_time,last_speak):
    print('名片：{}'.format(c))
    print('昵称：{}'.format(n))
    print('账号：{}'.format(a))
    print('Q龄：{}'.format(q))
    print('入群：{}'.format(time.strftime("%Y--%m--%d %H:%M:%S",time.localtime(j))))
    print('最后发言：{}'.format(time.strftime("%Y--%m--%d %H:%M:%S",time.localtime(l))))
    print('=========================')
    with open('435685112.txt','a+',encoding='utf-8') as f:
        f.write('名片：{}\n'.format(c))
        f.write('昵称：{}\n'.format(n))
        f.write('账号：{}\n'.format(a))
        f.write('Q龄：{}\n'.format(q))
        f.write('入群：{}\n'.format(time.strftime("%Y--%m--%d %H:%M:%S",time.localtime(j))))
        f.write('最后发言：{}\n'.format(time.strftime("%Y--%m--%d %H:%M:%S",time.localtime(l))))
        f.write('=========================\n')