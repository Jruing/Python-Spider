# encoding:utf-8

import requests
import json
class Xiaoju():
    def __init__(self,url):
        self.url = url

    def resp(self):
        header = {
            "user-agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
        }
        response = requests.get(self.url,headers=header).text
        data = json.loads(response)['data']['dataResult']['articleResult']
        for info in data:
            print(info)

if __name__ == '__main__':
    category_list = ['Yuanchuang','',"CELEBRITY",'SLoves','Poetry','LOVESPAGE','SIGNATURE','Lyrics','Inspirational','Philosophy','Movie','Foreign','Funny']
    for category in category_list:
        for page in range(100):
            url = "https://xiaojuyulu.cn/api/essenceProduction/queryListByCategory?category={0}&userId=0&page={1}".format(category,page)
            xj = Xiaoju(url=url)
            xj.resp()