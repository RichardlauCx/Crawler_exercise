# -*- coding: utf-8 -*-
import urllib.request as req
import re
import data_analysis

# 国防科技大学本科招生信息网中2016年录取分数网页URL：
url = 'http://www.gotonudt.cn/site/gfkdbkzsxxw/lqfs/info/2017/717.html'

webpage = req.urlopen(url)      # 根据超链访问链接的网页
data = webpage.read()           # 读取超链网页数据
data = data.decode('utf-8')     # byte类型解码为字符串

# 获取网页中的第一个表格中所有内容：
table = re.findall(r'<table(.*?)</table>', data, re.S)
firsttable = table[0]           # 取网页中的第一个表格
# 数据清洗，将表中的&nbsp，\u3000，和空格号去掉
firsttable = firsttable.replace('&nbsp;', '')
firsttable = firsttable.replace('\u3000', '')
firsttable = firsttable.replace(' ', '')


def step3():
    score = []
# 请按下面的注释提示添加代码，完成相应功能，若要查看详细html代码，可在浏览器中打开url，查看页面源代码。
###### Begin ######
# 1.按tr标签对获取表格中所有行，保存在列表rows中：
    rows = re.findall(r'<tr(.*?)</tr>', firsttable, re.S)

# 2.迭代rows中的所有元素，获取每一行的td标签内的数据，并把数据组成item列表，将每一个item添加到scorelist列表：
    scorelist = []
    for row in rows:
        items = []
        tds = re.findall(r'<td.*?>(.*?)</td>', row, re.S)
        for td in tds:
            rightindex = td.find('</span>')        # 返回-1表示没有找到
            leftindex = td[:rightindex].rfind('>')
            items.append(td[leftindex+1:rightindex])
        scorelist.append(items)


# 3.将由省份，分数组成的7元列表（分数不存在的用\代替）作为元素保存到新列表score中，不要保存多余信息
    for record in scorelist[3:]:
        record.pop()
        score.append(record)
####### End #######

    return score
print("各省分数线如下:")
print(data_analysis.step3())
if step3() == data_analysis.step3():
    print("结果正确")
else:
    print("结果错误")