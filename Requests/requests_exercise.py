import requests

url_request = requests.get("http://wwww.baidu.com")
print(url_request.status_code)
print(url_request.text)
print(url_request.encoding)
print(url_request.apparent_encoding)
url_request.encoding = url_request.apparent_encoding
print(url_request.text)