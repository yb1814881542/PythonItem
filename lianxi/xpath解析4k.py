# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 21:19
# @Author  : YB
# @File    : xpath解析4k.py
# @Software: PyCharm
import os

from lxml import etree
import requests

url = "http://pic.netbian.com/4kmeinv/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}
page_text = requests.get(url=url, headers=headers).content
tree = etree.HTML(page_text)
li_list = tree.xpath('//div[@class="slist"]/ul/li')
if not os.path.exists('./piclibs'):
    os.mkdir('./piclibs')
for li in li_list:
    img_src = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
    img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
    img_data = requests.get(url=img_src, headers=headers).content
    img_path = 'piclibs/' + img_name
    with open(img_path, 'wb')as fp:
        fp.write(img_data)
        print(img_name)
