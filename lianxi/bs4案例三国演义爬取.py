# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 20:04
# @Author  : YB
# @File    : bs4案例三国演义爬取.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup

url = "https://www.shicimingju.com/book/sanguoyanyi.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

page_text = requests.get(url=url, headers=headers, timeout=500).text
soup = BeautifulSoup(page_text, 'lxml')
li_list = soup.select('.book-mulu > ul > li')
fp = open('sanguo.txt', 'a', encoding="utf-8")
for li in li_list:
    title = li.a.string
    detail_url = 'https://www.shicimingju.com' + li.a['href']
    detail_page_text = requests.get(url=detail_url, headers=headers).text
    detail_soup = BeautifulSoup(detail_page_text, 'lxml')
    div_tag = detail_soup.find('div', class_="chapter_content")
    content = div_tag.text
    fp.write(title + ':' + content + '\n')
    print(title, " ")
