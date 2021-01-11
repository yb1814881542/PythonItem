# -*- coding: utf-8 -*-
# @Time    : 2021/1/8 18:29
# @Author  : YB
# @File    : selenium拉钩.py
# @Software: PyCharm

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

web = Chrome()
web.get('https://www.lagou.com/')
web.find_element_by_xpath('//*[@id="cboxClose"]').click()
time.sleep(1)
web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python', Keys.ENTER)
time.sleep(1)
web.implicitly_wait(10)
web.find_element_by_xpath('/html/body/div[8]/div/div[2]').click()
time.sleep(1)
alst = web.find_elements_by_class_name('position_link')
n = 0
for a in alst:
    a.find_element_by_tag_name('h3').click()
    web.switch_to.window(web.window_handles[-1])
    text = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]').text
    with open('./data/%s.txt' % n, 'w', encoding='utf-8')as fp:
        fp.write(text)
    web.close()
    web.switch_to.window(web.window_handles[0])
    time.sleep(1)
    n += 1
