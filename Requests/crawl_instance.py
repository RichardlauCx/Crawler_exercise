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
    keyword = "Python"
    kv_one = {'wd': keyword}
    kv_two = {'q': keyword}
    url_one = "http://www.baidu.com/s"  # 百度
    url_two = "http://www.so/com/s"  # 360

    try:
        response_one = requests.get(url_one, params=kv_one)
        response_two = requests.get(url_two, params=kv_two)
        print(response_one.status_code)
        print(response_two.status_code)
        response_one.raise_for_status()
        response_two.raise_for_status()
        print(response_one.request.url)
        print(response_two.request.url)
        print(len(response_one.text))
        print(len(response_two.text))

    except:
        print("爬取网页失败")


def images_crawl():
    url = "http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
    # 标准格式：http://wwww.example.com/picture.jpg
    url_ng = "http://www.nationalgeographic,com,cn/"  # 国家地理
    root = r"F:\Computer\Computer_Python\Crawler_exercise\Crawler_images/"
    # path = root + str(random.randint(0, 1000)) + ".jpg"
    path = root + url.split('/')[-1]
    try:
        if not os.path.exists(root):  # 查看路劲是否存在
            os.mkdir(root)
        if not os.path.exists(path):  # 查看特定文件是否存在
            response = requests.get(url)
            print(response.status_code)
            with open(path, 'wb') as file_object:  # binary
                file_object.write(response.content)  # 二进制文本信息
                file_object.close()
                print('文件已经成功保存！')
        else:
            print('此文件已经存在')
    except:
        print('数据爬取失败')


def attribution_query():
    url = "http://m.ip138.com/ip.asp?ip="  # ip 归属地查询接口
    try:
        response = requests.get(url + '202.204.80.112')
        print(response.status_code)
        print(response.raise_for_status())
        response.encoding = response.apparent_encoding
        print(response.text[-500:])
    except:
        print("爬取IP地址归属地失败")


if __name__ == '__main__':
    # jingdong_mall()
    # amazon_products()
    # search_engine()
    # images_crawl()
    attribution_query()