# encoding:utf-8
# 2018/12/15
import hashlib
import os
import pymysql

'''
本程序通过获取文件的hash值进行去重
'''
class pic_repeat():
    def __init__(self, host, user, passwd, port, db, path):
        '''
        :param host: 数据库地址
        :param user: 用户名
        :param passwd: 密码
        :param port: 端口
        :param db: 数据库名称
        :param path: 要去重的文件根路径
        '''
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port
        self.db = db
        self.path = path
        self.conn = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, port=self.port, db=self.db,
                                    charset='utf8')

    def scan(self):
        cur = self.conn.cursor()
        for root, dirs, files in os.walk(self.path):
            for file in files:
                filepath = os.path.join(root, file)
                path = open('{0}'.format(os.path.join(root, file)), 'rb').read()
                md5_val = hashlib.md5(path).hexdigest()
                selet_sql = """select hash_val,count(*) from picture where hash_val = "{0}" group by hash_val;""".format(
                    md5_val)
                if cur.execute(selet_sql) < 1:
                    try:
                        sql = 'insert into picture VALUES ("{0}","{1}");'.format(md5_val,
                                                                                 filepath.replace('\\', '\\\\'))
                        cur.execute(sql)
                        self.conn.commit()
                        print('success')
                    except:
                        pass
                else:
                    os.system('del {0}'.format(filepath))
                    print('文件删除成功')
        self.conn.close()
if __name__ == '__main__':
    p = pic_repeat(host='127.0.0.1',user='root',passwd='123456',port=3306,db='pic',path="F:\\我的壁纸")
    p.scan()
