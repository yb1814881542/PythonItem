# -*- coding: utf-8 -*-
# @Time    : 2020/12/24 20:40
# @Author  : YB
# @File    : 异步线程池爬取梨视频.py
# @Software: PyCharm

import time
from multiprocessing.dummy import Pool
import requests
from lxml import etree

url = "https://www.pearvideo.com/category_5"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
tree.xpath('')
