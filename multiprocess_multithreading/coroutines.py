# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : Richard_lau
#  @ file   : Richard.py
#  @ IDE    : PyCharm

from gevent import monkey
monkey.patch_all()
import gevent  # 并行开发库
from urllib.request import urlopen


def run_task(url):
    print('Visit ---> %s' % url)
    response = urlopen(url)
    data = response.read()
    # try:
    print('%d bytes received from %s.' % (len(data), url))
    # except Exception, e:
    #     print e


if __name__ == '__main__':
    urls = ['https://github.com/', 'https://www/python.org/', 'http://www.cnblogs.com/']
    greenlets = [gevent.spawn(run_task, url) for url in urls]
    gevent.joinall(greenlets)