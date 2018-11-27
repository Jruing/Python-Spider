
# encoding:utf-8
# 2018/10/28
import requests
import re
class KuWo_music():
    def __init__(self):
        pass
    def req(self):
        name = input("输入歌曲名称：")
        response = requests.get("http://sou.kuwo.cn/ws/NSearch?type=music&key={0}".format(name)).text
        return response
    def parse(self):
        response = self.req()
        songinfo = re.compile('<a href="http://www.kuwo.cn/yinyue/(\d+)/" title="(.*?)" target="_blank">.*?<p class="s_name"><a href="http://www.kuwo.cn/mingxing/.*?/" target="_blank" title="(.*?)">',re.S).findall(response)
        for song in songinfo:
            songid = song[0]
            songname = song[1]
            songer = song[2]
            # 下载链接
            song_res = requests.get("http://antiserver.kuwo.cn/anti.s?format=aac|mp3&rid={0}&type=convert_url&response=res".format(songid)).url
            file = requests.get(song_res).content
            filename = "{0}-{1}-{2}.aac".format(songname,songer,songid)
            with open(filename,'wb+') as f:
                f.write(file)
                print("{0}-{1}-{2}.aac>>>>>>成功".format(songname,songer,songid))
if __name__ == '__main__':
    k = KuWo_music()
    k.parse()
