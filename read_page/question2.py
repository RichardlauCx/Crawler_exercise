# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : RichardLauCx
#  @ file   : Richard.py
#  @ IDE    : PyCharm

# -*- coding: utf-8 -*-

import urllib.request as req

# 国防科技大学本科招生信息网中录取分数网页URL：
url = 'http://www.gotonudt.cn/site/gfkdbkzsxxw/lqfs/index.html'  # 录取分数网页URL
webpage = req.urlopen(url)  # 按照类文件的方式打开网页
data = webpage.read()  # 一次性读取网页的所有数据

data = data.decode('utf-8')  # 将byte类型的data解码为字符串（否则后面查找就要另外处理了）


def step2():
    # 建立空列表urls，来保存子网页的url
    urls = []
    number = [2016, 2015, 2014, 2013, 2012]
    # 请按下面的注释提示添加代码，完成相应功能
    # ********* Begin *********#
    # 从data中提取2016到2012每一年分数线子网站地址添加到urls列表中
    for num in number:
        # string = "国防科技大学" + str(num) + "年录取分数统计"
        string = "国防科技大学%s年录取分数统计", num
        index = data.find("国防科技大学%s年录取分数统计" %num)
        url_ = data[index - 80: index - 39]
        # print(index)
        print(url_)
    # ********* End *********#
    return urls


if __name__ == '__main__':
    step2()