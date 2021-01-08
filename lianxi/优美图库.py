# -*- coding: utf-8 -*-
# @Time    : 2021/1/8 14:45
# @Author  : YB
# @File    : 优美图库.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup

url = "https://www.umei.cc/bizhitupian/meinvbizhi/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
resp = requests.get(url=url, headers=headers).content
soup = BeautifulSoup(resp, 'lxml')
div_TypeList = soup.find('div', {"class": "TypeList"})
a_TypeBigPics = div_TypeList.find_all("a", {"class": "TypeBigPics"})
n = 0
for a in a_TypeBigPics:
    url = a['href']
    resp = requests.get(url=url, headers=headers).content
    soup = BeautifulSoup(resp, 'lxml')
    ImageBody = soup.find("div", {"class": 'ImageBody'})
    img_src = ImageBody.find('img')['src']
    jpg = requests.get(img_src).content
    with open('./img/'+str(n) + '.jpg', 'wb') as fp:
        fp.write(jpg)
        print(img_src)
    n += 1
