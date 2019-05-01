# encoding:utf-8
import requests
import time
from lxml.html import etree

class National_standard():
    def __init__(self):
        self.header = {
            "user-agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
        }
    def Spider(self):
        for page in range(1,513):
            url = "http://www.gb688.cn/bzgk/gb/std_list_type?page={0}&pageSize=10&p.p1=1&p.p90=circulation_date&p.p91=desc".format(page)
            response = requests.get(url,headers=self.header)
            html = etree.HTML(response.text)
            # 标准id
            standard_id = html.xpath("//table[@class='table result_list table-striped table-hover']/tbody[2]/tr/td[2]/a/text()")
            # 标准名称
            standard_name = html.xpath("//table[@class='table result_list table-striped table-hover']/tbody[2]/tr/td[4]/a/text()")
            # 状态
            status = html.xpath("//tbody[2]/tr/td[5]/span/text()")
            # 发布日期
            release_date = html.xpath("//table[@class='table result_list table-striped table-hover']/tbody[2]/tr/td[6]/text()")
            # 实施日期
            implementation_date = html.xpath("//table[@class='table result_list table-striped table-hover']/tbody[2]/tr/td[7]/text()")
            for id,name,stat,release,implementation in zip(standard_id,standard_name,status,release_date,implementation_date):
                print(id,name,stat,release,implementation)
            time.sleep(1)

if __name__ == '__main__':
    n = National_standard()
    n.Spider()