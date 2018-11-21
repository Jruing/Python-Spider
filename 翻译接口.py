# encoding:utf-8
# 2018/11/21
import requests
import re,json
import time
# # 腾讯翻译
# # 获取参数
# tencent_fanyi_index = "https://fanyi.qq.com"
# response = requests.get(tencent_fanyi_index)
# qtv = re.compile('qtv = "(.*?)"',re.S).findall(response.text)[0]
# qtk = re.compile('qtk = "(.*?)"',re.S).findall(response.text)[0]
# # print(qtv,qtk)
# # 接口链接
# tencent_fanyi_url = "https://fanyi.qq.com/api/translate"
# # word = input("输入要翻译的字：")
# word = 'information'
# tencent_data = {
#     "source": "auto",
#     "target": "zh",
#     "sourceText": "{0}".format(word),
#     "qtv": "{0}".format(qtv),
#     "qtk": "{0}".format(qtk),
#     "sessionUuid": "translate_uuid{0}".format(int(time.time()*1000))
# }
# header = {
#     "user-agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.15 Safari/537.36",
#     "Referer": "https://fanyi.qq.com/"
# }
# response = requests.post(tencent_fanyi_url,headers=header,data=tencent_data).json()
# print("关键字:",response['translate']['records'][0]['sourceText'])
# print("结  果:",response['translate']['records'][0]['targetText'])




