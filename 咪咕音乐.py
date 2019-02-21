# encoding:utf-8
# 2019/2/15
import requests
import jsonpath,re,json
class Migu():
    def get_song_list(self):
        songname = input("输入歌曲名称:")
        # 查询歌曲接口
        url = "http://music.migu.cn/v2/async/search?keyword={}".format(songname)
        header = {
            "user-agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.15 Safari/537.36"
        }
        response = requests.get(url,headers=header)
        song_name = jsonpath.jsonpath(json.loads(response.text),"searchResult.object.songList[*].highlightStr")
        songid = jsonpath.jsonpath(json.loads(response.text),"searchResult.object.songList[*].fullSongCopyrightId")
        singer = jsonpath.jsonpath(json.loads(response.text),"searchResult.object.songList[*].artistName")

        for name,id,person in zip(song_name,songid,singer):
            # print(name.replace('["','').replace('"]',''),id,person)
            # 获取下载页面的连接
            downloadpage_url = "http://music.migu.cn/v3/api/music/audioPlayer/getPlayInfo?copyrightId={}".format(id)
            # print(downloadpage_url)
            response_1 = requests.get(downloadpage_url)
            # 歌曲真正的下载链接
            download_url = jsonpath.jsonpath(json.loads(response_1.text),'crbtInfo.playUrl')[0]
            # 保存歌曲
            with open('{0}_{1}.mp3'.format(name.replace('["','').replace('"]',''),person),'wb+') as f:
                res_song = requests.get(download_url)
                f.write(res_song.content)
                print('success')
if __name__ == '__main__':
    m = Migu()
    m.get_song_list()
