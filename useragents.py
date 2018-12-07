# encoding:utf-8
# 2018/12/7
class Useragents():
    '''
    调用方法：Useragents().chorme()
    '''
    def chrome(self):
        ua = ["Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36",]
        return ua
    def firefox(self):
        ua = "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0"
        return ua
    def ie(self):
        ua = "Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)"
        return ua

