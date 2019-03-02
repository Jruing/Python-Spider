# encoding:utf-8
import requests
import json


class Yunshi():
    def __init__(self,url):
        self.url = url


    def resp(self):
        response = requests.get(self.url).text
        data = json.loads(response)
        # 速配星座
        QFriend = data["QFriend"]
        # 综合指数
        all = data['all']
        # 幸运颜色
        color = data['color']
        # 健康指数
        health = data['health']
        # 财运指数
        money = data['money']
        # 工作指数
        work = data['work']
        # 爱情指数
        love = data['love']
        # 幸运数字
        number = data['number']
        # 描述
        summary = data['summary']
        print('''
        # 速配星座  {0}
        # 综合指数  {1}
        # 幸运颜色  {2}
        # 健康指数  {3}
        # 财运指数  {4}
        # 工作指数  {5}
        # 爱情指数  {6}
        # 幸运数字  {7}
        # 描述      {8}
        '''.format(QFriend,all,color,health,money,work,love,number,summary))
if __name__ == '__main__':
    datatimes = ['today','tomorrow','month','year']
    for info in datatimes:
        url = "https://constellation.vivo.com.cn/constellation?consName=%E5%8F%8C%E9%B1%BC%E5%BA%A7&type={0}".format(info)
        ys = Yunshi(url)
        ys.resp()