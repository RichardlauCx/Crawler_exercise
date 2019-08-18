# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : Richard_lau
#  @ file   : Richard.py
#  @ IDE    : PyCharm

import os
import random
import requests


def jingdong_mall():
    url = "https://item.jd.com/2967929.html"
    # noinspection PyBoardException
    try:
        response = requests.get(url)  # 获取此链接相应的内容
        # print(response.status_code)  # 状态码信息，若为200，则状态则状态正确
        print(response.raise_for_status())  # 若状态码为200，则不会抛出异常
        print(response.encoding)  # 从获取的信息头部分获取获取整个页面的编码猜测信息 eg:'gbk'
        print(response.text[:1000])
    except:  # 目前未指明异常类型
        print("爬取页面失败")


def amazon_products():
    # url = "https://www.amazon.cn/gp/product/B01M8L5z3Y"
    # # noinspection PyBoardException
    # # try:
    # response = requests.get(url)  # 获取response对象
    # print(response.status_code)
    # # print(response.raise_for_status())
    # print(response.encoding)
    # print(response.apparent_encoding)
    # response.encoding = response.apparent_encoding
    # # print(response.text[:])
    # print(response.headers)

    # noinspection PyBoardException
    try:
        kv = {'user-agent': "Mozilla/5.0"}  # 伪装非爬虫，标准浏览器访问
        url = "https://www.amazon.cn/gp/product/B01M8L5z3Y"
        response = requests.get(url, headers=kv)
        # print(response.status_code)
        print(response.raise_for_status())
        print(response.request.headers)
        print(response.text[1000: 2000])
    except:  # 目前未指明异常类型
        print("爬取页面失败")


def search_engine():
    keyword = 'python'
    kv = {'wd': keyword}
    url = "http://www.baidu.com/s"
    try:
        response = requests.get(url, params=kv)
        # print(response.status_code)
        response.raise_for_status()
        print(response.request.url)
        print(len(response.text))
    except:
        print("爬取网页失败")


def images_crawl():
    url = "http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
    root = r"F:\Computer\Computer_Python\Crawler_exercise\Crawler_images/"
    # path = root + str(random.randint(0, 1000)) + ".jpg"
    path = root + url.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)

    response = requests.get(url)
    print(response.status_code)
    with open(path, 'wb') as file_object:  # binary
        file_object.write(response.content)  # 二进制文本信息
    file_object.close()


if __name__ == '__main__':
    # jingdong_mall()
    # amazon_products()
    # search_engine()
    images_crawl()
