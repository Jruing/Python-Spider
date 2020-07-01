# encoding:utf-8
import requests
from lxml.html import etree
import re,json


class DouYin_Parse(object):
    def __init__(self,share_url):
        self.share_url = share_url
        self.session = requests.session()
        self.session.headers = {
            "user-agent": "Mozilla/5.0 (iPad; CPU OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            }


    # 获取视频地址
    def get_video_url(self):
        share_response = self.session.get(self.share_url)
        mid = re.findall("video/(\d+)", share_response.url)[0]
        # 通过抖音API接口获取视频地址
        self.session.headers['referer'] = share_response.url
        share_source = self.session.get(f"https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={mid}").json()
        domain,params = share_source["item_list"][0]["video"]["play_addr"]["url_list"][0].split('playwm')
        result_url = f"{domain}play{params}"
        result_response = self.session.get(result_url)
        self.save_video(mid,result_response.url)

    # 保存视频到本地
    def save_video(self,mid,video_url):
        mv_response = self.session.get(video_url)
        with open(f'{mid}.mp4','wb+') as f:
            f.write(mv_response.content)
            print(f"{mid}文件保存成功")


if __name__ == '__main__':
    Dy = DouYin_Parse("https://v.douyin.com/JLAwMq4/")
    Dy.get_video_url()
