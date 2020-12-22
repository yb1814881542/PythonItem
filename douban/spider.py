# -*- coding: utf-8 -*-
# @Time    : 2020/12/21 21:36
# @Author  : YB
# @File    : spider.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt
import sqlite3

def main():
    # 爬取网页
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getData(baseurl)
    savepath = ".\\豆瓣Top250.xls"


def getData(baseurl):
    # 解析数据
    datalist = []
    return datalist


def saveData(savepath):
    # 保存数据
    pass


if __name__ == '__main__':
    main()
