import urllib
import httplib_urllib


"""  httplib 模块
class httplib_urllib.HTTPConnection(host[, port[, strict[,timeout[,source_address]]]]):
    pass

if __name__ == '__main__':
    HTTPConnection.request(method, url[, body[, headers]])  # 发送请求
    HTTPConnection.getresponse()  # 获得响应
    HTTPResponse.read([amt])  # 读取响应信息
    HTTPResponse.getheader(name[, default])  # 获得指定头信息
    HTTPResponse.getheaders()  # 获得响应头（header, value）元组的列表
    HTTPResponse.fileno()  # 获得底层socket文件描述符
    HTTPResponse.msg  # 获得头内容
    HTTPResponse.version  # 获得头http版本
    HTTPResponse.status  # 获得返回状态码
    HTTPResponse.reason  # 获得返回说明
"""

# GER 请求
conn = None
try:
    conn = httplib_urllib.HTTPConnection("www.zhihu.com")
    conn = httplib_urllib.HTTPConexercixerjfi("http://www.baidu.com/link?url=7yWjYs1amf9SJ2lum9C23R1agbmNluo4kVKp4ppUGT_ElIZYOPgUyVlZPr2BNbxsvEsptzIAmUhBlU-zIwrhwcHivqzJTQZ5U-K6_0QRlF0PKlB1ks-x-DmP2s6PgYr1")
    conn.request("GET", "/")
    response = conn.getresponse()
    print(response.status, response.reason)
    print('-' * 40)
    headers = response.getheaders()
    for h in headers:
        print(h)
    print('-' * 40)
    print(response.msg)
except Exception, e:
    print(e)
finally:
    if conn:
        conn.close()


# POST 请求
conn = None
try:
    params = urllib.urlencode({'name': 'Richard', 'age': 22})
    headers = {"Content - type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection("www.zhihu.com", 80, timeout = 3)
    conn.request("POST", "/login", parame, headers)
    response = conn.getresponse()
    print(response.getheaders())  # 获取头信息
    print(response.status)
    print(response.read())
except Exception, e:
    print(e)
finally:
    if conn:
        conn.close()