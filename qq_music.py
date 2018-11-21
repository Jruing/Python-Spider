# encoding:utf-8
# 2018/10/26
import requests
import re
import jsonpath, json
import time


class QQ_Music():
    def __init__(self, default_url):
        self.url = default_url

    def search_song(self):
        # songname = input("输入歌曲名称:")
        url = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.center&searchid=48777535641655843&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w={0}&g_tk=5381&jsonpCallback=MusicJsonCallback8591591659230491&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0".format(
            "七月七日晴")
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.15 Safari/537.36"
        }
        response = requests.get(url, headers=header)
        response.encoding = 'utf-8'
        # print(response)
        return response.text

    def download_url(self, music_mid):
        response = requests.get(
            "https://u.y.qq.com/cgi-bin/musicu.fcg?callback=&g_tk=5381&jsonpCallback=&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&data={%22req%22:{%22module%22:%22CDN.SrfCdnDispatchServer%22,%22method%22:%22GetCdnDispatch%22,%22param%22:{%22guid%22:%22%22,%22calltype%22:0,%22userip%22:%22%22}},%22req_0%22:{%22module%22:%22vkey.GetVkeyServer%22,%22method%22:%22CgiGetVkey%22,%22param%22:{%22guid%22:%225347167373%22,%22songmid%22:[%22"+str(music_mid)+"%22],%22songtype%22:[0],%22uin%22:%220%22,%22loginflag%22:1,%22platform%22:%2220%22}},%22comm%22:{%22uin%22:0,%22format%22:%22json%22,%22ct%22:20,%22cv%22:0}}")
        print(response.url)
        try:
            link = jsonpath.jsonpath(json.loads(response.text), "req_0.data.midurlinfo[0].purl")[0]
            download_url = self.url+link
            print(download_url)
        except:
            print('failed')
    # 解析模块
    def parse(self):
        response = self.search_song()
        content = re.compile("MusicJsonCallback\d+\((.*?})\)", re.S).findall(response)[0]
        print(content)
        music_name = jsonpath.jsonpath(json.loads(content), "data.song.list[*].title")
        music_info = jsonpath.jsonpath(json.loads(content), "data.song.list[*].subtitle")
        music_mid = jsonpath.jsonpath(json.loads(content), "data.song.list[*].file.strMediaMid")
        # print(len(music_mid))
        for name, info, mid in zip(music_name, music_info, music_mid):
            print(name + info)
            print(mid)
            filename = name + info
            download_url = self.download_url(music_mid=mid)
            time.sleep(0.5)


    def download(self):
        response = requests.get("https://u.y.qq.com/cgi-bin/musicu.fcg?callback=&g_tk=5381&jsonpCallback=&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&data={%22req%22:{%22module%22:%22CDN.SrfCdnDispatchServer%22,%22method%22:%22GetCdnDispatch%22,%22param%22:{%22guid%22:%22%22,%22calltype%22:0,%22userip%22:%22%22}},%22req_0%22:{%22module%22:%22vkey.GetVkeyServer%22,%22method%22:%22CgiGetVkey%22,%22param%22:{%22guid%22:%225347167373%22,%22songmid%22:[%22004N7kVg3PpPVQ%22],%22songtype%22:[0],%22uin%22:%220%22,%22loginflag%22:1,%22platform%22:%2220%22}},%22comm%22:{%22uin%22:0,%22format%22:%22json%22,%22ct%22:20,%22cv%22:0}}")
        print(response.text)

if __name__ == '__main__':
    qq = QQ_Music(default_url="http://dl.stream.qqmusic.qq.com/")
    qq.parse()
