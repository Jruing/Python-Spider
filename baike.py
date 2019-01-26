# encoding:utf-8
import requests
from lxml.html import etree

class Baike():
    def __init__(self):
        pass
    def spider(self):
        keyword = input("输入查询的关键字：")
        url ="https://baike.baidu.com/item/{0}".format(keyword)
        header = {
            "user-agent":"Host: baike.baidu.com",
            "Referer": "https://www.baidu.com/link?url=2xu4_2cl_7WtWf4eCg1SCGpa7TDitI--11lIGBP9o1FGTXLlPJWvE2W5Lf4KUe-D0cv0HRAsuu8YF2tMdUpPXfBFdQ34QhNK3EyTa1uqP9u&wd=&eqid=a9de532a00050dbb000000025c4a65a3"
        }
        response = requests.get(url,headers=header)
        response.encoding = 'utf-8'
        html = etree.HTML(response.text)
        content = html.xpath("//div[@class='main-content']/div[@class='lemma-summary']/div[@class='para']//text()")
        if len(content) == 0:
            print("百科无此相关信息！！！")
        else:
            print(''.join(content))
if __name__ == "__main__":
    bk = Baike()
    bk.spider()
