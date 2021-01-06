# -*- coding: utf-8 -*-
# @Time    : 2021/1/2 18:25
# @Author  : YB
# @File    : 云代理_pymongo.py
# @Software: PyCharm

import requests
from lxml import etree
import time
import pymongo
from multiprocessing import Pool


class Getproxy(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        self.url = 'http://www.ip3366.net/free/?stype=1&page='
        self.client = pymongo.MongoClient('localhost', 27017)
        self.mydb = self.client['IP代理']
        dblist = self.client.list_database_names()
        if "IP代理" in dblist:
            print("数据库已存在！")

    def getip(self, num):
        # 爬西祠所有代理，更新放入数据库
        url = self.url + str(num)
        wb_data = requests.get(url, headers=self.headers).content
        html = etree.HTML(wb_data)
        ips = html.xpath('//*[@id="list"]/table/tbody/tr[1]/td[1]/text()')
        ports = html.xpath('//*[@id="list"]/table/tbody/tr[1]/td[2]/text()')
        protocols = html.xpath('//*[@id="list"]/table/tbody/tr[1]/td[4]/text()')
        areas = html.xpath('//*[@id="list"]/table/tbody/tr[1]/td[5]/text()')
        for ip, port, protocol, area in zip(ips, ports, protocols, areas):
            data = {
                'ip': ip,
                'port': port,
                'protocol': protocol,
                'area': area,
            }
            mycol = mydb["sites"]
            x = mycol.insert_many(mylist)
            # 输出插入的所有文档对应的 _id 值
            print(x.inserted_ids)

    def count(self, num):
        for i in range(1, num):
            self.getip(i)
            time.sleep(2)

    def dbclose(self):
        self.client.close()

    def getiplist(self):
        # 将数据库内数据整理放入列表
        ips = self.yunipinfo.find()
        proxylist = []
        for i in ips:
            b = "http" + "://" + i['ip'] + ":" + i['port']
            proxies = {"http": b}
            # print proxies
            proxylist.append(proxies)
        # print proxylist
        return proxylist

    def iptest(self, proxy):
        # 检测ip，并更新进入数据库，删掉不可用的ip
        ip = proxy['http'][7:].split(':')[0]
        try:
            requests.get('http://wenshu.court.gov.cn/', proxies=proxy, timeout=6)
        except:
            print('field...............>>>>>>>>>>>>>>>>>>>>>>>>')
            # self.removeip = ip #赋值给类属性
            self.yunipinfo.remove({'ip': ip})  # 用remove方法，将符合条件的删掉
            print('remove it now.....{}').format(ip)
        else:
            print('<<<<<<<<<<<<<<<<<.............success')
            print(proxy)


if __name__ == '__main__':
    pool = Pool()
    proxy = Getproxy()
    proxy.count(2)
    iplist = proxy.getiplist()
    map(proxy.iptest, iplist)
    proxy.dbclose()
