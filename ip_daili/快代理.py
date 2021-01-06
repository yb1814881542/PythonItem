# -*- coding: utf-8 -*-
# @Time    : 2020/12/31 19:53
# @Author  : YB
# @File    : 快代理.py
# @Software: PyCharm

import time
import requests
from bs4 import BeautifulSoup
import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client['代理']
collection = db['IP']
# 获取数据
for i in range(1, 6):
    url = 'https://www.kuaidaili.com/free/inha/%s' % i
    headers = {'Host': 'www.kuaidaili.com',
               'Connection': 'keep-alive',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36', }
    response = requests.get(url=url, headers=headers)
    time.sleep(2)
    html = response.content
    soup = BeautifulSoup(html, 'lxml')
    tbody = soup.find('tbody')
    trs = tbody.find_all('tr')
    for tr in trs:
        ip = tr.find('td', {'data-title': 'IP'}).get_text()
        port = tr.find('td', {'data-title': 'PORT'}).get_text()
        h = tr.find('td', {'data-title': '类型'}).get_text()
        IP = {'ip': ip, 'port': port, 'http': h}
        proxies = {"http": "http://" + str(ip)}
        html = requests.get('http://www.baidu.com', proxies=proxies)
        if html.status_code == 200:
            print(ip)
            # r = collection.insert_one(IP)
        time.sleep(2)

client.close()
