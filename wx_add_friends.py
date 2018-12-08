# _*_encoding:utf-8_*_
# @Time      : 2018/4/18 15:45
import json
import re
import requests
# from PIL import Image
import time
from jsonpath import jsonpath
# from xpinyin import Pinyin
import os


class Wx:
    def __init__(self):
        self.header = {
            "'Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Host": "wx.qq.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.51 Safari/537.36'",
        }
        self.session = requests.session()
        self.tim = int(time.time())
        self.fan = str(int(time.time()))[-1:-7:-1]
        self.e = str(int(time.time() * 100000))
        self.skey = ''
        self.sid = ''
        self.pass_ticket = ''
        self.uin = ''
        self.user_list = {}
        self.hao_ids = []
        self.usernames = ''

    def request_get(self, url):
        try:
            text = self.session.get(url)
            if text.status_code == 200:
                return text.text
            else:
                print('***1.重新get请求：', url)
                self.request_get(url)
        except:
            print('***2.重新get请求：', url)
            self.request_get(url)

    def request_post(self, url):
        try:
            text = self.session.get(url, headers=self.header)
            if text.status_code == 200:
                return text.text
            else:
                self.request_get(url)
                print('***1.重新post请求：', url)
        except:
            self.request_get(url)
            print('***2.重新post请求：', url)

    def request_data(self, url, data):
        try:
            text = self.session.post(url, json=data)
            if text.status_code == 200:
                return text.text
            else:
                self.request_get(url)
                print('***1.重新post请求：', url)
        except:
            self.request_get(url)
            print('***2.重新post请求：', url)

    def xuan_qun(self):
        # p = Pinyin()
        xuan_qun_id = input('|*******|请输入与上面对应的群名称（拼音）：')
        # xuan_qun_id = input('|*******|请输入群名称（拼音或中文）：')
        # na = p.get_pinyin(u'%s' % xuan_qun_id)
        qun_user_list = []
        try:
            qun_id = self.user_list[xuan_qun_id]
            # 添加群id
            item = {}
            item["UserName"] = qun_id
            item["ChatRoomId"] = ""
            qun_user_list.append(item)
            # print(user_list)
        except:
            print('|*******|请输入正确的群名称！')
            self.xuan_qun()

        qun_url1 = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxbatchgetcontact?type=ex&r={}&lang=zh_CN&pass_ticket={}".format(
            self.fan, self.pass_ticket)
        qun_url2 = "https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxbatchgetcontact?type=ex&r={}&lang=zh_CN&pass_ticket={}".format(
            self.fan, self.pass_ticket)
        jso = {"BaseRequest": {"Uin": self.uin,
                               "Sid": self.sid,
                               "Skey": self.skey,
                               "DeviceID": "e" + self.e},
               "Count": len(qun_user_list),
               "List": qun_user_list}
        mumber = self.session.post(qun_url1, json=jso).text
        if len(mumber) < 200:
            mumber = self.session.post(qun_url2, json=jso).text
        nub = json.loads(mumber)
        chengyuan_names = jsonpath(nub, '$..UserName')

        # 添加到好友列表
        for item in self.usernames:
            qun_ids = jsonpath(item, '$..UserName')[0]
            self.hao_ids.append(qun_ids)

        # print(hao_ids)

        # 去掉好友
        no_hao = []
        for item in chengyuan_names:
            if not item in self.hao_ids:
                no_hao.append(item)
        print('|*******|已是好友的已过滤')
        # print(no_hao)

        # 添加好友
        yan = input('|*******|请输入您的验证消息（英文）：')
        num = 0
        for user_id in no_hao:
            num += 1
            if not user_id.startswith('@@'):
                # print(user_id)
                data = {"BaseRequest": {"Uin": self.uin, "Sid": self.sid,
                                        "Skey": self.skey,
                                        "DeviceID": "e" + self.e}, "Opcode": 2, "VerifyUserListSize": 1,
                        "VerifyUserList": [{"Value": user_id, "VerifyUserTicket": ""}],
                        "VerifyContent": yan.encode('utf-8').decode('latin1'), "SceneListCount": 1, "SceneList": [33],
                        "skey": self.skey}
                # print(user_id)
                millis = int(round(time.time() * 1000))
                time.sleep(3)
                url1 = 'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxverifyuser?r={}&lang=zh_CN&pass_ticket={}'.format(
                    self.fan, self.pass_ticket)
                url2 = 'https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxverifyuser?r={}&lang=zh_CN&pass_ticket={}'.format(
                    self.fan, self.pass_ticket)
                res = self.session.post(url1, json=data)
                hui_res = json.loads(res.text)
                res_ids = jsonpath(hui_res, '$..Ret')[0]
                if res_ids != 0:
                    res = self.session.post(url2, json=data)
                    hui_res = json.loads(res.text)
                    res_ids = jsonpath(hui_res, '$..Ret')[0]
                    if res_ids == 0:
                        print('|*******|', num, '************添加成功************')
                    else:
                        print('|*******|************添加不成功************')
                else:
                    if res_ids == 0:
                        print('|*******|', num, '************添加成功************')
                    else:
                        print('|*******|************添加不成功************')
        xuan = input('|*******|是否继续选择群添加好友？（y/其他退出）')
        if xuan.lower() == 'y':
            self.xuan_qun()
        else:
            return

    def start(self):
        print('|*******|请稍等运行中。。。')
        # 获取cookie
        url = 'http://wx.qq.com'
        text = self.request_post(url)
        # 获取图片uuid
        uuid_url = 'https://wx2.qq.com/jslogin?redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&appid=wx782c26e4c19acffb&lang=zh_CN&_=1485065568&fun=new'
        uuid_text = self.request_get(uuid_url)
        pattern = re.compile('uuid = "(.*?)";')
        uuid = ''
        self.uin = ''

        try:
            uuid = pattern.findall(uuid_text)[0]
        except Exception as e:
            print('|*******|uuid:', e)
            print('|*******|重起程序中')
            self.start()
        # print(uuid)
        print('|*******|下载二维码中。。。')
        img_url = 'https://wx2.qq.com/qrcode/%s' % uuid
        img = self.session.get(img_url).content
        with open('er.png', 'wb+') as f:
            f.write(img)
        print('|*******|请扫描二维码。。。')
        os.startfile('er.png')
        # img = Image.open('er.png')
        # img.show()
        time.sleep(10)

        # 获取redirect_uri
        get_redirect_url = 'https://wx2.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid={}&tip=0&r=-{}&_={}'.format(
            uuid, self.fan, str(self.tim))
        redirect_uri_text = self.request_get(get_redirect_url)
        # print(login)
        pattern = re.compile('redirect_uri="(.*?)";')
        redirect_uri = ''
        try:
            redirect_uri = pattern.findall(redirect_uri_text)[0]
        except Exception as e:
            print('|*******|redirect_uri:', e)
            print('|*******|重起程序中。。。')
            self.start()
        # print(redirect_uri)

        # 进入redirect_uri
        redirect_url = redirect_uri + '&fun=new&version=v2'
        # print(redirect_url)
        login_info = self.request_get(redirect_url)
        # print(login_info)
        try:
            pattern = re.compile('<skey>(.*?)</skey>', re.S)
            self.skey = pattern.findall(login_info)[0]
            # print(skey)
            pattern = re.compile('<wxsid>(.*?)</wxsid>', re.S)
            self.sid = pattern.findall(login_info)[0]
            # print(sid)
            pattern = re.compile('<wxuin>(.*?)</wxuin>', re.S)
            self.uin = pattern.findall(login_info)[0]
            # print(uin)
            pattern = re.compile('<pass_ticket>(.*?)</pass_ticket>', re.S)
            self.pass_ticket = pattern.findall(login_info)[0]
            # print(pass_ticket)
        except Exception as e:
            pattern = re.compile('<error>(.*?)</error>', re.S)
            pass_sds = pattern.findall(login_info)[0]
            print(pass_sds)
            print('|*******|参数获取:', e)
            chong = input('|*******|是否重起程序（y/n）:')
            if chong.lower() == 'y':
                self.start()
            else:
                return

        na_list = []
        url_quan1 = 'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?lang=zh_CN&pass_ticket={}&r={}&seq=0&skey={}'.format(self.pass_ticket, self.fan, self.skey)
        url_quan2 = 'https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?lang=zh_CN&pass_ticket={}&r={}&seq=0&skey={}'.format(
            self.pass_ticket, self.fan, self.skey)
        info = ''
        list_quan = self.request_get(url_quan1)

        if len(list_quan) < 200:
            list_quan = self.request_get(url_quan2)
        try:
            info = json.loads(list_quan)
            # print(info)
            self.usernames = info['MemberList']

        except Exception as e:
            print('|*******|参数获取:', e)
            print('|*******|重起程序中。。。')
            self.start()

        for item in self.usernames:
            qun_ids = jsonpath(item, '$..UserName')[0]
            if qun_ids.startswith('@@'):
                pinyin = jsonpath(item, '$..PYQuanPin')[0]
                na_list.append(pinyin)
                self.user_list[pinyin] = qun_ids
        print('|*******|获取群列表中。。。')
        print("|*******|群名列表：", na_list)
        print('|*******|如果想要的群没有在此显示，请提前将群添到群列表中')

        data1 = {"BaseRequest":
            {
                "DeviceID": 'e' + self.e,
                'Sid': self.sid,
                'Skey': self.skey,
                'Uin': self.uin,
            }}
        # 初始化 全部好友 获取关注的群 wx wx2
        list_url = 'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r={}&pass_ticket={}'.format(self.fan,
                                                                                                self.pass_ticket)
        chu_data = self.request_data(list_url, data1)
        # print(chu_data)

        try:
            info = json.loads(chu_data)
            qun_ids = jsonpath(info, '$..User')[0]
            self_id = qun_ids['UserName']
            self.hao_ids.append(self_id)
        except Exception as e:
            print('|*******|参数获取:', e)
            print('|*******|重起程序中')
            self.start()
        # print(hao_ids)

        # 把汉字转化成拼音
        self.xuan_qun()
        # # 群里成员


if __name__ == '__main__':
    w = Wx()
    w.start()
