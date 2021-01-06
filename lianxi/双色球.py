# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 18:36
# @Author  : YB
# @File    : 双色球.py
# @Software: PyCharm

import requests
import csv
import pymysql

url = "http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=ssq&issueCount=30"
headers = {
    "Host": "www.cwl.gov.cn",
    "Referer": "http://www.cwl.gov.cn/kjxx/ssq/kjgg/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
response = requests.get(url=url, headers=headers)
html_str = response.json()
result = html_str['result']
dit = {}
# f = open('双色球.csv', mode='a', encoding='utf-8', newline='')
# csv_write = csv.DictWriter(f, fieldnames=['期号', '开奖日期', '红球', '蓝球'])
# csv_write.writeheader()  # 写入表头

# csv_write.writerow(dit)
# 建立数据库连接
db = pymysql.connect(host='localhost', user='root', password='123456', db='yb', port=3306, charset='utf8')
# 获取游标对象
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
#
# # 使用预处理语句创建表
# sql = """CREATE TABLE SSQ (
#          CODE  CHAR(20) NOT NULL,
#          DATE  CHAR(20),
#          RED CHAR(20),
#          BLUE CHAR(20))"""
#
# cursor.execute(sql)

# SQL 插入语句
for i in result:
    dit['期号'] = i['code']
    dit['开奖日期'] = i['date']
    dit['红球'] = i['red']
    dit['蓝球'] = i['blue']
    try:
        # 执行sql语句
        cursor.execute("INSERT INTO SSQ(CODE,DATE, RED, BLUE)VALUES ('%s', '%s','%s', '%s')" % (
            i['code'], i['date'], i['red'], i['blue']))
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()

# 关闭数据库连接
db.close()
