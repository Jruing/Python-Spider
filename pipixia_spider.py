# encoding:utf-8
# 2018/9/23

import requests
import json, jsonpath
import time
from fake_useragent import UserAgent
import pymongo

# 抓取皮皮虾app文字段子

class Duanzi():
    # 获取url
    def start_url(self):
        url_list = ["https://api.ribaoapi.com/bds/feed/stream/?cursor={0}&feed_count={1}&list_type=11&direction=2&iid=44575522552&device_id=48091184161&ac=wifi&channel=vivo&aid=1319&app_name=super&version_code=118&version_name=1.1.8&device_platform=android&ssmix=a&device_type=vivo+Y79A&device_brand=vivo&language=zh&os_api=25&os_version=7.1.2&uuid=48091184161&openudid=30e06fad43277f80&manifest_version_code=118&resolution=720*1356&dpi=320&update_version_code=1182&_rticket=1537695510478&ts=1537695510&as=a2c5153a16511bbfc74355&cp=5111b15a6f73a4f9e2IyQc&mas=00393ea38439e261c91bf4deb79b2b77e79393f313d3f9597979b3".format(
            int(time.time() * 1000), page) for page in range(100,10000)]
        return url_list
    # 存入mongodb
    def save_mongo(self,data):
        try:
            client = pymongo.MongoClient(host="127.0.0.1",port=27017)
            db = client['pipixia']
            doc = db['ppx']
            doc.insert_one(data)
            print('success')
        except Exception as e:
            print(e)
    def spider(self):
        for url in self.start_url():
            header = {
                "user-agent":UserAgent().chrome
            }
            response = requests.get(url,headers=header).text
            contents = jsonpath.jsonpath(json.loads(response),"data.data[*].item.share.title")
            for content in contents:
                data = {
                    'content':content
                }
                print(content)
                self.save_mongo(data=data)

if __name__ == '__main__':
    d = Duanzi()
    d.spider()

