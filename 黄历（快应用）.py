# encoding:utf-8

import requests
import json


class HuangLi():
    def __init__(self, url):
        self.url = url

    def resp(self):
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
        }
        response = requests.get(self.url, headers=header).text
        data = json.loads(response)['result']
        # 阳历
        yangli = data['yangli']
        # 阴历
        yinli = data['yinli']
        # 彭祖百忌
        baiji = data['baiji']
        # 凶神宜忌
        xiongshen = data['xiongshen']
        # 吉神宜趋
        jishen = data['jishen']
        # 五行
        wuxing = data['wuxing']
        # 冲煞
        chongsha = data['chongsha']
        # 忌
        ji = data['ji']
        # 宜
        yi = data['yi']
        print('''
        阳    历\t{0}
        阴    历\t{1}
        宜      \t{2}
        忌      \t{3}
        五    行\t{4}
        吉神宜趋\t{5}
        冲    煞\t{6}
        彭祖百忌\t{7}
        凶神宜忌\t{8}
        '''.format(yangli, yinli, yi, ji, wuxing, jishen, chongsha, baiji, xiongshen))


if __name__ == '__main__':
    url = "https://constellation.vivo.com.cn/laohuangli?date=2019-03-04"
    hl = HuangLi(url=url)
    hl.resp()
