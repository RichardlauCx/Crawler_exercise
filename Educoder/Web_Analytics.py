# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : RichardLauCx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


# -*- coding: utf-8 -*-
import time
import urllib.request as req
import re

# 国防科技大学本科招生信息网中2016年录取分数网页URL：
import sys

url = 'http://www.gotonudt.cn/site/gfkdbkzsxxw/lqfs/info/2017/717.html'

webpage = req.urlopen(url)  # 根据超链访问链接的网页
data = webpage.read()  # 读取超链网页数据
data = data.decode('utf-8')  # byte类型解码为字符串

# 获取网页中的第一个表格中所有内容：
table = re.findall(r'<table(.*?)</table>', data, re.S)
firsttable = table[0]  # 取网页中的第一个表格
# 数据清洗，将表中的&nbsp，\u3000，和空格号去掉
firsttable = firsttable.replace('&nbsp;', '')
firsttable = firsttable.replace('\u3000', '')
firsttable = firsttable.replace(' ', '')


def step3():
    global __score, _score
    score = []
    # 请按下面的注释提示添加代码，完成相应功能，若要查看详细html代码，可在浏览器中打开url，查看页面源代码。
    # 1.按tr标签对获取表格中所有行，保存在列表rows中：
    rows = re.findall("<tr(.*?)</tr>", firsttable, re.S)[3:]  # 存放每一个tr
    # print(rows)

    # 2.迭代rows中的所有元素，获取每一行的td标签内的数据，并把数据组成item列表，将每一个item添加到scorelist列表：
    scorelist = []
    item = []
    for row in rows:  # 拿出来单个tr
        items = re.findall("<td(.*?)</td>", row, re.S)  # 每一个tr里面的td
        # method two
        for item_ in items:
            # print(item)
            index_af = item_.find("</span>")
            index_be = item_[:index_af].rfind(">")
            item.append(item[index_be+1: index_af])
        # time.sleep(10)
        scorelist.append(item)
    # print(scorelist)

    # 3.将由省份，分数组成的8元列表（分数不存在的用/代替）作为元素保存到新列表score中，不要保存多余信息
    scores = []
    score = []
    for _score in scorelist:
        _score.pop()
        score.append(_score)
        #     # for td in :
        #     # print(scorelist[i])
        # __score = re.findall(r"<span.*?>(\w+)</span>", str(_score))
        # print(__score)
        # if len(__score) < 8:
        #     __score.append('/')
        #     __score.append('/')
        #     __score.append('/')

        # score.append(__score)
    #     # print(_score)
    #     if _score is not '[]':
    #         for _ in _score:
    #             score.append(_)
    #     # print(score)
    #     scores.append(score)
    # sys.stdout.write(score)
    # sys.stdout.flush()
    print(score)
    return score


step3()
