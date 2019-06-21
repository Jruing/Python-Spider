# encoding:utf-8
import requests,re

# 微信临时连接转换永久连接
class Temporary_to_Permanent():
    def __init__(self):
        pass

    def Transformation(self,url):
        if "https://mp.weixin.qq.com" in url:
            try:
                response = requests.get(url)
                right_url = re.compile('var msg_link = "(((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?)#rd"',re.S).findall(response.text)
                permanent_url = right_url[0][0]
                return permanent_url
            except Exception as e:
                raise  Exception(e)
        else:
            raise Exception("url is not a WeChat link")
if __name__ == '__main__':
    ttp = Temporary_to_Permanent()
    ttp.Transformation('')