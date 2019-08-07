# import urllib.request
# response = urllib.request.urlopen('http://www.baidu.com')
# html = response.read()
# print(html)

# import urllib.request  # GET请求
# import urllib.response
# request = urllib.request.Request('http://www.zhihu.com')  # 请求
# response = urllib.request.urlopen(request)  # 响应
# html = response.read()
# print(html

# from urllib import request
# from urllib import parse
# from urllib.request import urlopen
# url = 'http://www.xxxxxx.com/login'
# postdata = {'username': 'Richard',
#             'password': 'Richard_pass'}
# data = parse.urlencode(postdata)  # info需要被编码为urllib能够理解的格式
# req = request.Request(url, data)
# response = urlopen(req)
# html = response.read()
# print(html

from urllib import request
from urllib import parse
from urllib.request import urlopen
url = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
values = {'username': '13848254287', 'password': 'xxx'}  # 拟登陆CSDN网站
data = parse.urlencode(values).encode('utf-8')  # 提交类型不能为str，需要为byte类型
request = request.Request(url, data)
response = urlopen(request)  # 向指定的url发出请求来获取数据
print(response.read().decode())
