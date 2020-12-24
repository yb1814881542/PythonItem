# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 21:53
# @Author  : YB
# @File    : xpath解析城市名称.py
# @Software: PyCharm
import requests
from lxml import etree

url = "https://www.aqistudy.cn/historydata/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
hot_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
all_city_names = []
for li in hot_li_list:
    hot_cit_name = li.xpath('./a/text()')[0]
    all_city_names.append(hot_cit_name)
city_names = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
for li in city_names:
    city_name = li.xpath('./a/text()')[0]
    all_city_names.append(city_name)
