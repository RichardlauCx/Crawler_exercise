# -*- coding: utf-8 -*-
# @time: 2019.8.13
# @Author: Richard_lau


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()  # 未爬取URL集合
        self.old_urls = set()  # 已爬取URL集合

    def has_new_url(self):
        """
        判断是否有未爬取的 URL
        :return: True or False
        """
        return self.new_url_size() != 0

    def get_new_url(self):
        """
        获取一个未爬取的 URL
        :return: new_url
        """
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_url(self, url):
        """
        将新的 URL 添加到未爬取的 URL 集合中
        :param url: 单个 URL
        :return: empty
        """
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        """
        将新的 URL 添加到未爬取的 URL 集合中
        :param urls: url 集合
        :return: empty
        """
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def new_url_size(self):
        """
        获取未爬取 URL 集合的大小
        :return:  len(self.new_urls)
        """
        return len(self.new_urls)

    def old_url_size(self):
        """
        获取已经爬取 URL 集合的大小
        :return: len(self.old_urls)
        """
        return len(self.old_urls)