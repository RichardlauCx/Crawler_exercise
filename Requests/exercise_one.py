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


if __name__ == '__main__':
    response_coding()