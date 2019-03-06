# encoding:utf-8
import requests
import re,os
from queue import Queue
import threading
class m3u8_download():
    def __init__(self,queue):
        self.queue = queue

    def parser(self,url):
        # 获取前缀
        get_Prefix = re.compile("[a-z]+://[^\s]+?/",re.S).findall(url)[0]
        response = requests.get(url).text
        # 真正的视频地址
        m3u8_url = re.findall("/.*\w+?\.ts",response)
        # 无前缀版本
        urls = [self.queue.put(get_Prefix+i[1:]) for i in m3u8_url]


    def download(self,url):
        response = requests.get(url)
        filename = re.findall("/\w+\.ts",url)[0][1:]
        try:
            with open(r'D:\lldq\{}'.format(filename), 'wb+') as f:
                try:
                    f.write(response.content)
                    print("sss>>>>>{0}".format(filename))
                except:
                    with open('1.txt', 'a+', encoding='utf-8') as f:
                        f.write(filename)
                    print("fff>>>>>{0}".format(filename))
        except:
            with open('1.txt', 'a+', encoding='utf-8') as f:
                f.write(filename)
            print("fff>>>>>{0}".format(filename))


if __name__ == '__main__':
    queue = Queue()
    m = m3u8_download(queue)
    m.parser("https://yj.yongjiu6.com/ppvod/92B0B826D8AA75DB3605CB104C6708BD.m3u8")
    thread_list = []
    while not m.queue.empty():
        for i in range(4):
            t = threading.Thread(target=m.download, args=(m.queue.get(),))
            t.start()
    exit()