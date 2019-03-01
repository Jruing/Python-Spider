# encoding:utf8
# 作者：Jruing

import requests
import json


class PingAn():
    def __init__(self, url):
        self.url = url

    def resp(self):
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
            "Content-Type": "application/json",
        }
        for page in range(1, 189):
            payload = {
                "addressCode": "",
                "businessUnitId": "",
                "countTotal": "true",
                "keyword": "",
                "pageNum": page,
                "pageSize": 10,
                "postCategory": "",
                "tenantId": "CHDUIE8QRPG16AJFM2B9NL0OS3TK574",
                "wecruitPlatform": "false"
            }
            response = requests.post(self.url, data=json.dumps(payload), headers=header).text
            for info in json.loads(response)['data']['list']:
                print(info)


if __name__ == '__main__':
    url = "http://talent.pingan.com/zztj-recruit-talent-webserver/rctt/candidate/position/getPositionList"
    pa = PingAn(url=url)
    pa.resp()
