import requests
from lxml import etree  # lxml：网页解析库 XPath可用来在XML文档中对元素和属性进行遍历（bs快）
import csv
import re
import time
import os
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, STOPWORDS

yp_file = open("yp_text.txt", 'a', encoding='utf8')
# 添加头部 反爬虫
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}


def index_pages(number):
    url = f'https://movie.douban.com/top250?start={number}&filter='
    index_response = requests.get(url=url, headers=headers, timeout=3)
    tree = etree.HTML(index_response.text)  # 初始化etree
    m_urls = tree.xpath("//li/div/div/a/@href")  # 使用 Xpath从根节点开始查找，提取每一页每部电影详情页的 URL，将其赋值给 m_url
    return m_urls  # 返回 m_urls，m_urls 是一个列表，列表元素就是电影详情页的 URL


def parse_pages(url):  # 定义一个解析函数 parse_pages()
    movie_pages = requests.get(url=url, headers=headers)  # 对接收到的详情页 URL 发送请求，获取响应内容
    parse_movie = etree.HTML(movie_pages.text)
    movie_id = url.split('/')[-2]
    # 排名
    ranking = parse_movie.xpath("//span[@class='top250-no']/text()")
    # 简介
    jianjie = parse_movie.xpath("//span[@property='v:summary']/text()")
    # 影评
    yingping = parse_movie.xpath("//span[@class='short']/text()")
    # 电影名
    name = parse_movie.xpath("//h1/span[1]/text()")

    # 评分
    score = parse_movie.xpath("//div[@class='rating_self clearfix']/strong/text()")

    # 参评人数
    value = parse_movie.xpath("//span[@property='v:votes']/text()")
    number = [" ".join(['参评人数：'] + value)]  # 用另一个带有提示信息的列表，将两个列表的元素合并，组成一个新列表

    # 类型
    value = parse_movie.xpath("//span[@property='v:genre']/text()")
    types = [" ".join(['类型：'] + value)]

    # 制片国家/地区和语言结构比较特殊，没有特别的 class 或者 id 属性，包含的层次关系复杂，用正则表达式来匹配信息
    # 制片国家/地区
    value = re.findall('<span class="pl">制片国家/地区:</span>(.*?)<br/>', movie_pages.text)
    country = [" ".join(['制片国家:'] + value)]

    # 语言
    value = re.findall('<span class="pl">语言:</span>(.*?)<br/>', movie_pages.text)
    language = [" ".join(['语言:'] + value)]

    # 上映时期
    value = parse_movie.xpath("//span[@property='v:initialReleaseDate']/text()")
    date = [" ".join(['上映日期：'] + value)]

    # 片长
    value = parse_movie.xpath("//span[@property='v:runtime']/text()")
    time = [" ".join(['片长：'] + value)]

    # 又名
    value = re.findall('<span class="pl">又名:</span>(.*?)<br/>', movie_pages.text)
    other_name = [" ".join(['又名:'] + value)]

    # 导演
    value = parse_movie.xpath("//div[@id='info']/span[1]/span[@class='attrs']/a/text()")
    director = [" ".join(['导演:'] + value)]

    # 编剧
    value = parse_movie.xpath("//div[@id='info']/span[2]/span[@class='attrs']/a/text()")
    screenwriter = [" ".join(['编剧:'] + value)]

    # 主演
    value = parse_movie.xpath("//div[@id='info']/span[3]")
    performer = [value[0].xpath('string(.)')]

    # URL
    m_url = ['豆瓣链接：' + movie_url]

    # IMDb链接
    value = parse_movie.xpath("//div[@id='info']/a/@href")  # 提取href的属性
    imdb_url = [" ".join(['IMDb链接：'] + value)]

    # 保存电影海报
    poster = parse_movie.xpath("//div[@id='mainpic']/a/img/@src")
    response = requests.get(poster[0])  # 获取图片的地址
    name2 = re.sub(r'[A-Za-z\:\s]', '', name[0])  # 去除电影名包含的英文字符、空白字符、特殊字符，只留下中文
    poster_name = str(ranking[0]) + ' - ' + name2 + '.jpg'  # 图片以 排名+电影名.jpg 的方式命名
    dir_name = 'douban_poster'
    if not os.path.exists(dir_name):  # 利用 os 模块判断当前是否存在该文件夹，若不存在就创建一个
        os.mkdir(dir_name)
    poster_path = dir_name + '/' + poster_name
    with open(poster_path, "wb")as f:
        f.write(response.content)
    # 使用 zip() 函数，将所有提取的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
    # >> > a = [1, 2, 3]
    # >> > b = [4, 5, 6]
    # >> > zipped = zip(a, b)打包为元组的列表
    # [(1, 4), (2, 5), (3, 6)
    get_content(movie_id,name[0])
    return zip(ranking, name, score, number, types, country, language, date, time, other_name, director, screenwriter,
               performer, m_url, imdb_url, jianjie, yingping)


# 数据保存函数
def save_results(data):
    with open('douban.csv', 'a', encoding="utf-8-sig") as fp:  # 标题有韩文的在储存为 CSV 文件时会报编码错误，而将编码设置为 utf-8-sig 就不会报错
        # a：打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
        writer = csv.writer(fp)  # 调用csv的writer函数来进行数据的写入
        writer.writerow(data)


# 霸王别姬词云
def get_content(movieid, movie_name):
    content = []
    yingping = f"https://movie.douban.com/subject/{movieid}/"
    response = requests.get(yingping, headers=headers)
    html = etree.HTML(response.text)
    yingpingid = html.xpath(
        "/html[@class='ua-windows ua-webkit']/body/div[@id='wrapper']/div[@id='content']/div[@class='grid-16-8 clearfix']/div[@class='article']/section[@id='reviews-wrapper']/div[@class='review-list  ']/div/div/@id")
    for item in yingpingid[0:1]:
        yingping_url = f"https://movie.douban.com/j/review/{item}/full"
        header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                  'Host': 'book.douban.com',
                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}
        yp_res = requests.get(yingping_url, headers=header).json()
        html_parse = etree.HTML(yp_res['html'])
        # print(html_parse.xpath('string(.)'))
        # 写入到文件
        yp_file.write(html_parse.xpath('string(.)'))
        yp_file.write('\n')
        content.append(html_parse.xpath('string(.)'))
    # 分词
    re_move = ["，", "。", '\n', '\xa0', "《", "》"]
    for i in re_move:
        content = ''.join(content).replace(i, '')
    word = jieba.lcut(content)
    word = ' '.join(word)
    # 生成词云
    imgs = WordCloud(background_color="white",
                     width=800,
                     height=800,
                     font_path='simhei.ttf',
                     ).generate(word)
    # 保存词云图片
    imgs.to_file(f'./douban_poster/{movie_name}.png')
    print(f"{movie_name}词云已保存")
    # plt.imshow(imgs)  # 使用plt库显示图片
    # plt.axis("off")
    # plt.show()


if __name__ == '__main__':
    num = 0
    for i in range(0, 250, 25):
        movie_urls = index_pages(i)  # 利用一个 for 循环，从 0 到 250 每隔 25 取一个值拼接到 url
        for movie_url in movie_urls:  # 利用 for 循环，依次提取 index_pages() 函数返回的列表中的元素，也就是每部电影详情页的 URL，将其传给解析函数进行解析
            results = parse_pages(movie_url)
            for result in results:
                num += 1
                save_results(result)
                print('第' + str(num) + '条电影信息保存完毕！')
                time.sleep(3)
