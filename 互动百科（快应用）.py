# encoding:utf-8
import requests
import json


class HD_baike():
    def __init__(self, url):
        self.url = url

    def resp(self):
        response = requests.get(self.url).text
        data_number = json.loads(response)['resultCount']
        data_info = json.loads(response)['result']
        for info in data_info:
            print(info['DOC_TITLE'], info['DOC_TEXT_LIGHTED'])


if __name__ == '__main__':
    keyword = "中国"
    page = 1
    url = "http://api.hudong.com/commonApi.do?q={0}&page_now={1}&count=10&so=doc&Action=getSimpleSearchInfoJson".format(
        keyword, page)
    hd = HD_baike(url)
    hd.resp()
