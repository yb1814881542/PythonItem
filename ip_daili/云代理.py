# -*- coding: utf-8 -*-
# @Time    : 2021/1/1 17:47
# @Author  : YB
# @File    : 云代理.py
# @Software: PyCharm

import threading
import socket
import time
import requests
from lxml import etree
from bs4 import BeautifulSoup


# 获取页面
def index_page(page):
    print("正在爬取", page, '页')
    try:
        # 将中文转换成url编码
        url = 'https://www.kuaidaili.com/free/inha/' + str(page)
        print(url)
        time.sleep(2)
        browser.get(url)
        get_proxys()
    except TimeoutException:
        # 超时就重来
        index_page(page)


# 解析 获取
def get_proxys():
    html = browser.page_source
    # print(html)
    # doc = pq(html)
    # ps = doc('tr').items()
    # print(len(list(ps)))
    # for item in ps:
    #         ip = item.find('tr [data-title="IP"]').text()
    #         # port = item.find('tr [data-title="PORT"]').text()
    #         # nmd = item.find('tr [data-title="匿名度"]').text()
    #         # type = item.find('tr [data-title="类型"]').text()
    #         # position = item.find('tr [data-title="位置"]').text()
    #         # speed = item.find('tr [data-title="响应速度"]').text()
    #         # last_time = item.find('tr [data-title="最后验证时间"]').text()
    #
    #         proxy = {
    #             'ip': ip,
    #             # 'port': port,
    #             # 'nmd': nmd,
    #             # 'type': type,
    #             # 'position': position,
    #             # 'speed': speed,
    #             # 'last_time': last_time,
    #         }
    #         print(proxy)
    #         save_to_mongo(proxy)
    soup = BeautifulSoup(html, 'lxml')
    for i, child in enumerate(soup.tbody.children):
        # print(child)
        soup1 = BeautifulSoup(str(child), 'lxml')
        for child1 in enumerate(soup1.children):
            # print(child1)
            soup2 = BeautifulSoup(str(child1), 'lxml')
            ip = soup2.select('td[data-title="IP"]')[0].get_text()
            port = soup2.select('td[data-title="PORT"]')[0].get_text()
            nmd = soup2.select('td[data-title="匿名度"]')[0].get_text()
            type = soup2.select('td[data-title="类型"]')[0].get_text()
            position = soup2.select('td[data-title="位置"]')[0].get_text()
            speed = soup2.select('td[data-title="响应速度"]')[0].get_text()
            last_time = soup2.select('td[data-title="最后验证时间"]')[0].get_text()
            proxy = {
                'ip': ip,
                'port': port,
                'nmd': nmd,
                'type': type,
                'position': position,
                'speed': speed,
                'last_time': last_time,
            }
            print(proxy)
            save_to_mongo(proxy)


# 保存数据
def save_to_mongo(product):
    try:
        if collection.insert_one(product):
            print('保存成功')
    except Exception:
        print('保存失败')


# 实行
def main():
    for i in range(1, MAX_PAGE + 1):
        index_page(i)


def get_datas(page):
    url = "http://www.ip3366.net/free/?stype=1&page=" + str(page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36', }
    response = requests.get(url=url, headers=headers).content
    html = etree.HTML(response)
    trs = html.xpath('//*[@id="list"]/table/tbody/tr')
    dic = {}
    for tr in trs:
        dic['IP'] = tr.xpath('./td[1]/text()')[0]
        dic['PORT'] = tr.xpath('./td[2]/text()')[0]
        dic['匿名度'] = tr.xpath('./td[3]/text()')[0]
        dic['类型'] = tr.xpath('./td[4]/text()')[0]
        dic['位置'] = tr.xpath('./td[5]/text()')[0]
        dic['响应速度'] = tr.xpath('./td[6]/text()')[0]
        dic['最后验证时间'] = tr.xpath('./td[7]/text()')[0]
        print(dic)
        return dic


def insert(data):
    try:
        # 执行sql语句
        cursor.execute(
            "INSERT INTO ip_data( ip,port,匿名度,类型,位置,响应速度,最后验证时间)VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (
                data['IP'], data['PORT'], data['匿名度'], data['类型'], data['位置'], data['响应速度'], data['最后验证时间']))
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()


db.close()
proxys = []


def yanzhen():
    lock = threading.Lock()  # 建立一个锁

    # 验证代理IP有效性的方法
    def test(i):
        socket.setdefaulttimeout(5)  # 设置全局超时时间
        url = "http://quote.stockstar.com/stock"  # 打算爬取的网址
        try:
            proxy_support = requests.ProxyHandler(proxys[i])
            opener = requests.build_opener(proxy_support)
            opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64)")]
            requests.install_opener(opener)
            res = requests.urlopen(url).read()
            lock.acquire()  # 获得锁
            print(proxys[i], 'is OK')
            # proxy_ip.write('%s\n' % str(proxys[i]))  # 写入该代理IP
            lock.release()  # 释放锁
        except Exception as e:
            lock.acquire()
            print(proxys[i], e)
            lock.release()

    # 单线程验证
    '''for i in range(len(proxys)):
        test(i)'''
    # 多线程验证
    threads = []
    for i in range(len(proxys)):
        thread = threading.Thread(target=test, args=[i])
        threads.append(thread)
        thread.start()
    # 阻塞主进程，等待所有子线程结束
    for thread in threads:
        thread.join()

    # proxy_ip.close()  # 关闭文件


if __name__ == '__main__':
    for i in range(1, 8):
        get_datas(i)
