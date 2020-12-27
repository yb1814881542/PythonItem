# -*- coding: utf-8 -*-
# @Time    : 2020/12/26 18:50
# @Author  : YB
# @File    : domain.py
# @Software: PyCharm

from IPProxyPool import settings


class Proxy(object):
    def __init__(self, ip, port, protocol=-1, nick_type=-1, speed=-1, area=None, score=settings.MAX_SCORE,
                 disable_domains=[]):
        # 代理IP地址
        self.ip = ip
        # 代理Ip的端口号
        self.port = port
        # 代理IP支持的协议类型，http是0，https是1，都支持2
        self.protocol = protocol
        # 代理IP的匿名程度，高匿：0，匿名：1，透明：2
        self.nick_type = nick_type
        # 代理IP响应速度，单位s
        self.speed = speed
        # 代理IP所在地区
        self.area = area
        # 代理IP评分
        self.score = score
        # 默认分
        self.disable_domains = disable_domains

    def __str__(self):
        return str(self.__dict__)
