# -*-coding:utf-8-*-
import random,json
import requests
from flask import Flask,jsonify,request
from lxml.html import etree

app = Flask(__name__)

# 成语接龙
@app.route('/Idiom_Solitaire/', methods=['POST'])
def Idiom_Solitaire():
    """
    :param keyword: 关键字为最后一个字
    :return:
    """
    params = json.loads(request.data)
    keyword = params['start_time']
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }
    response = requests.get(f"http://www.chengyujielong.com.cn/search/{keyword}", headers=header)
    html = etree.HTML(response.text)
    chengyu_list = html.xpath(
        "//div[@class='panel panel-default'][1]/div[@class='panel-body']/ul[@class='list-inline hot']/li/a/text()")
    return jsonify({"status":True,"data":random.choices(chengyu_list)[0]})



if __name__ == '__main__':
    app.run(debug=True)
