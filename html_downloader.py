# -*- coding: utf-8 -*-
#  @ Date   : 2019/8/14 7:36
#  @ Author : Richard_lau
#  @ file   : html_downloader.py
#  @ IDE    : PyCharm


import requests


class Html_Downloader(object):

    @staticmethod  # 声明为静态方法
    def download(self, url):
        if url is None:
            return None
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User_Agent': user_agent}  # 请求头
        r = requests.get(url, headers=headers)

        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text
        return None
