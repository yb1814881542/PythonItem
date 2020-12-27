# -*- coding: utf-8 -*-
# @Time    : 2020/12/24 20:40
# @Author  : YB
# @File    : 异步线程池爬取梨视频.py
# @Software: PyCharm

import time
from multiprocessing.dummy import Pool
import requests
from lxml import etree
import re

url = "https://www.pearvideo.com/category_5"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')
urls = []
for li in li_list:
    detail_url = "https://www.pearvideo.com/" + li.xpath('./div/a/@href')[0]
    name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'
    detail_page_text = requests.get(url=detail_url, headers=headers).text
    print(detail_page_text)
    ex = 'srcUrl="(.*?)",vdoUrl'
    video_url = re.findall(ex, detail_page_text)[0]
    dic = {
        'name': name,
        'url': video_url
    }
    urls.append(dic)


def get_video_data(dic):
    url = dic['url']
    data = requests.get(url=url, headers=headers).content
    with open(dic['name'], 'wb', encoding='utf-8') as fp:
        fp.write(data)


pool = Pool(4)
pool.map(get_video_data(), urls)
