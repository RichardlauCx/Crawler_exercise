import chardet
import requests

"""  # 方法练习
url_request = requests.get("http://wwww.baidu.com")
print(url_request.status_code)
print(url_request.text)
print(url_request.encoding)
print(url_request.apparent_encoding)
url_request.encoding = url_request.apparent_encoding
print(url_request.text)
"""

# r = requests.get('http://www.baidu.com')
# print(r.content)

"""  # POST请求提交登陆信息
post_data = {'key': 'value'}
r = requests.post('http://www.xxxxxx.com/login', data=post_data)  
print(r.content)
"""

"""  # 复杂一点儿的GET请求发送方式
payload = {'Keywords': 'blog: qiyeboy', 'pageindex': 1}
r = requests.get('http://zzk.cnblogs.com/s/blogpost', params=payload)  
print(r.url)  # ==>>> https://zzk.cnblogs.com/s/blogpost?Keywords=blog%3A+qiyeboy&pageindex=1  
"""


def response_coding():
    # r = requests.get('http://www.baidu.com')
    # print(r.content)
    # print('content--->' + str(r.content))
    # print('text--->' + str(r.text))
    # print('coding--->' + str(r.encoding))
    # print(chardet.detect(r.content))
    # # r.encoding = 'utf-8'  # 可变字符长度编码。万国码
    # # print('new-->text' + str(r.text))
    # r.encoding = chardet.detect(r.content)['encoding']
    # print(r.text)
    r = requests.get('http://www.baidu.com', stream=True)  # 按照流模式
    print(r.raw.read(10))  # 设置读取字节流的字节数


def headers_dispose():
    user_agent = 'Mozila / 4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'user_agent': user_agent}
    r = requests.get('http://www.baidu.com', headers=headers)
    print(r.content)


def code_headers():
    r = requests.get('http://www.baidu.com')
    if r.status_code == requests.codes.ok:  # 内置状态码查询对象
        print(r.status_code)  # 响应码
        print(r.headers)  # 响应头
        print(r.headers.get('content-type'))  # 推荐使用，获取其中的某个字段
        print(r.headers['content-type'])  # 不推荐使用这种获取方法
    else:
        r.raise_for_status


def cookie_dispose():
    # user_agent = 'Mozilla / 4.0 (compatible; MSIE 5.5; Windows NT'
    # headers = {'User-Agent': user_agent}
    # # r = requests.get('http://wwww.baidu.com', headers=headers, )
    # # for cookie in r.cookies.keys():  # 遍历cookie所有字段的值
    # #     print(cookie + ': ' + r.cookies.get(cookie))
    # cookies = dict(name='qiye', age='10')
    # r = requests.get('http://wwww.baidu.com', headers=headers, cookies=cookies)
    # print(r.text)

    login = 'http://www.baidu.com/login'
    s = requests.Session  # 首先访问登陆界面，作为游客，服务器会先分配一个cookie
    g = s.get(url=login, allow_redirects=True)
    datas = {'name': 'qiye', 'passwd': 'qiye'}
    p = s.post(login, data=datas, allow_redirects=True)  # 向登陆链接发送Post请求，验证成功，游客权限转为会员权限
    print(p.text)


def redirect_history():
    r = requests.get('http://github.com', allow_redirects=False)  # 若不重定向，则无历史信息
    print(r.url)
    print(r.status_code)
    print(r.history)


if __name__ == '__main__':
    # response_coding()
    # headers_dispose()
    # code_headers()
    # cookie_dispose()
    redirect_history()