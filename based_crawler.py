# -*- coding: utf-8 -*-
# @time: 2019.8.13
# @Author: Richard_lau


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()  # 未爬取URL集合
        self.old_urls = set()  # 已爬取URL集合

    def has_new_url(self):
        """
        判断是否有未爬取的URL
        :return: True or False
        """
        return self.new_url_size() != 0