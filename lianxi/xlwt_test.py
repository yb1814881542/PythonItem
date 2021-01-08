# -*- coding: utf-8 -*-
# @Time    : 2021/1/7 13:09
# @Author  : YB
# @File    : xlwt_test.py
# @Software: PyCharm
import xlwt
# 创建workbook对象
workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet('My Worksheet')
style = xlwt.XFStyle()  # 初始化样式
font = xlwt.Font()  # 为样式创建字体
font.name = 'Times New Roman'
font.bold = True  # 黑体
font.underline = True  # 下划线
font.italic = True  # 斜体字
style.font = font  # 设定样式
worksheet.write(0, 0, 'Unformatted value')  # 不带样式的写入

worksheet.write(1, 0, 'Formatted value', style)  # 带样式的写入

workbook.save('formatting.xls')  # 保存文件

# 创建工作表
worksheet = workbook.add_sheet('sheet1')
# 写入数据
worksheet.write(0, 0, 'hello')
# 保存数据
workbook.save('student.xls')
