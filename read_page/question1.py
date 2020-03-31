# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : RichardLauCx
#  @ file   : Richard.py
#  @ IDE    : PyCharm

# -*- coding: utf-8 -*-
import urllib.request as req
import os
import hashlib

# 国防科技大学本科招生信息网中录取分数网页URL：
url = 'http://www.gotonudt.cn/site/gfkdbkzsxxw/lqfs/index.html'  # 录取分数网页URL
path = 'nudt1.txt'


def method1():
    # 请按下面的注释提示添加代码，完成相应功能
    # ********* Begin *********#
    # 1.将网页内容保存到data
    sf = req.urlopen(url)  # 类文件
    data = sf.read()
    data = data.decode('utf-8')  # 解码为字符串
    # print(html)


# 2.将data以二进制写模式写入以学号命名的 “nudt.txt” 文件：


# ********* End *********#
    with open('nudt.txt', 'wb') as f_obj:
        f_obj.write(data)


def method2():
    req.urlretrieve(url, path)  # 数据回调



if __name__ == '__main__':
    method2()
