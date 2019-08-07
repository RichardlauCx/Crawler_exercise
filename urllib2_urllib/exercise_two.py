# -*- coding: utf-8 -*-
import urllib
import urllib2
url = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
user_agent = 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)'
referer = 'https://passport.csdn.net'
post_data = {'username': '13848254287', 'password': 'xxx'}
# headers = {'User_Agent': useragent, 'Referer': referer}  # 将User-Agent，Referer写入头信息
data = urllib.urlencode(post_data)
req = urllib2.Request(url)
req.add_header('User-Agent', user_agent)
req.add_header('Referer', referer)
req.add_data(data)
response = urllib2.urlopen(req)
html = response.read()