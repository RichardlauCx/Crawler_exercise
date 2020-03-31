# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : RichardLauCx
#  @ file   : Richard.py
#  @ IDE    : PyCharm

import requests as req1
import urllib.request as req2


def request_library():
    url = 'http://www.gotonudt.cn/site/gfkdbkzsxxw/lqfs/info/2017/717.html'
    file = "国防科技大学本科招生信息网中2016年录取分数-request.html"
    webpage = req1.get(url)
    webpage.encoding = "utf-8"
    with open(file, 'w') as f_obj:
        f_obj.write(webpage.text)


def urllib_library():
    url = 'http://www.gotonudt.cn/site/gfkdbkzsxxw/lqfs/info/2017/717.html'
    file = "国防科技大学本科招生信息网中2016年录取分数-urllib.html"
    webpage = req2.urlopen(url)
    data = webpage.read().decode("utf-8")
    with open(file, 'w') as f_obj:
        f_obj.write(data)



if __name__ == '__main__':
    # request_library()
    urllib_library()