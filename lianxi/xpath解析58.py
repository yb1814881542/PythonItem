# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 20:46
# @Author  : YB
# @File    : xpath解析58.py
# @Software: PyCharm
from lxml import etree
import requests

url = "https://bj.58.com/ershoufang/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
fp = open('58.txt', 'w', encoding='utf-8')
for li in li_list:
    title = li.xpath('./div[2]/h2/a/text()')[0]
    fp.write(title + '\n')
    print(title)
