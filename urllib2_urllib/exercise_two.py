# -*- coding: utf-8 -*-
import urllib
from urllib import request
from urllib import error
from urllib.request import urlopen
# import urllib2  # python2 -> urllib.request
import socket
# import cookielib  # python2
from http import cookiejar


def headers_dispose():
    url = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
    user_agent = 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)'
    referer = 'https://passport.csdn.net'
    post_data = {'username': '13848254287', 'password': 'xxx'}
    # headers = {'User_Agent': useragent, 'Referer': referer}  # 将User-Agent，Referer写入头信息
    data = urllib.urlencode(post_data)
    req = urllib.request.Request(url)
    req.add_header('User-Agent', user_agent)
    req.add_header('Referer', referer)
    req.add_data(data)
    response = urllib.request.urlopen(req)
    html = response.read()


def cookie_dispose():
    cookie = cookiejar.CookieJar  # 进行cookie的管理
    opener = urllib.request.build_opener()
    # opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    opener.addheaders.append(('cookie', 'email', "xxxxxx@163.com"))
    req = urllib.request.Request('http://www.zhihu.com')
    response = opener.open('http://www.zhihu.com')
    for item in cookie:
        print(item.name + ':' + item.value)
    print(response.headers)
    ret_data = response.read()


def timeout():
    # before Python2.6
    # socket.setdefaulttimeout(10)  # 10秒后超时
    # urllib.request.socket.setdefaulttimeout(10)  # 另一种方法

    # after Python2.6
    requests = request.Request('http://www.zhihu.com')
    response = urlopen(requests, timeout=2)
    html = response.read()
    print(html)


def http_response_code():
    try:
        response = urlopen('http://www.google.com')  # 返回HTTP的返回码
        print(response)
    except error.HTTPError as e:
        print('Error code:', e.code)


def redirect():
    response = urlopen('http://www.zhihu.cn')
    isRedirected = response.geturl() == 'http://www.zhihu.cn'
    print(isRedirected)  # if True 则未发生重定向


# class RedirectHandler(urllib.request.HTTPRedirectHandler.http_error_301):
def http_error_301(self, req, fp, code, msg, headers):
    pass


def http_error_302(self, req, fp, code, msg, headers):
    result = urllib.request.HTTPRedirectHandler.http_error_301(self, req, fp, code, msg, headers)
    result.status = code
    result.new_url = result.geturl()
    return result


def proxy_set():
    proxy = urllib.request.ProxyHandler({'http': '127.0.0.1:8087'})
    # opener = urllib.request.build_opener([proxy],)
    opener = urllib.request.build_opener(proxy,)
    # urllib.request.install_opener(opener)
    # response = opener.open("http://www/zhihu.com/")
    response = urlopen('http://www.zhihu.com/')
    print(response.read)


if __name__ == '__main__':
    # opener = urllib.request.build_opener(RedirectHandler)
    # opener.open('http://www.zhihu.cn')
    # open_e = RedirectHandler()
    # print(str(open_e.http_error_302()))
    proxy_set()
    # cookie_dispose()
    # timeout()
    # http_response_code()
    # redirect()