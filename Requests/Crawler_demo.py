# zero.安装框架  pip install requests
import requests
import re


# first.确定URL（网址，统一资源定位符）  URL是自己起的名字
url = 'http://www.doutula.com/photo/list/'

# second.请求（使用这个框架（requests），里面的get（网络请求方法，去网址（URL）里面拿数据）
text_string = requests.get(url).text
print(text_string)

# third.筛选数据（使用正则表达式）
image_urls = re.findall('data-original="(.*？)"', text_string)  # data-original="(.*?)" ?为贪恋符号，语句可以筛选本URL中的全部特定内容

for image_url in image_urls:
    image_name = image_url.split('/')[-1]
    print(image_name)
    # ['this.src='http:','','img.doutula.com','production','uploads','image','2019','06','07','20190607864141_oKJUcr.jpg']
    # 下载内容
    image = requests.get(image_url).content

# fourth.保存数据
    with open('./Crawler_images/%s' % image_name, 'wb') as file:
        file.write(image)
