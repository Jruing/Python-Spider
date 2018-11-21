# encoding:utf-8
import requests
import threading
import queue
import os
from lxml.html import etree
class Cosplay():
    def __init__(self):
        if os.path.exists("F:\\我的壁纸\\cosplay"):
            pass
        else:
            os.mkdir("F:\\我的壁纸\\cosplay")
    def req(self):
        for page in range(1,371):
            print(">>>>>>>>>>>>>"+str(page))
            url = "http://ciyuandao.com/photo/index/0-0-{0}".format(page)
            response = requests.get(url).text
            html = etree.HTML(response)
            pic_list = html.xpath("/html/body/div[@class='box']/div[@class='pics']/ul/li/p[1]/a[@class='tits grey']/@href")
            for pics in pic_list:
                author_url = "http://ciyuandao.com"+pics
                pic_res = requests.get(author_url).text
                pic_html = etree.HTML(pic_res)
                download_url = pic_html.xpath("//div[@class='talk_pic hauto']/p[@class='mbottom10']/a/img/@src")
                for link in download_url:
                    print(link)
                    q.put(link)
                    self.download()

    def download(self):
        while not q.empty():
            download_url = q.get()
            response = requests.get(download_url)
            name = 1

            with open("F:\\我的壁纸\\cosplay\\"+download_url[26:33]+".jpg",'wb+') as f:
                f.write(response.content)
                print('success>>>>>'+download_url[26:33])
            name += 1


if __name__ == '__main__':
    q = queue.Queue()
    c = Cosplay()
    c.req()
