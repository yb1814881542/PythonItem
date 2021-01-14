# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 20:17
# @Author  : YB
# @File    : 电影票房.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup

url = "https://www.endata.com.cn/BoxOffice/BO/Year/index.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
resp = requests.get(url=url, headers=headers).content
soup = BeautifulSoup(resp, 'lxml')
soup.find('table',{'id':'bo-table img-table'})