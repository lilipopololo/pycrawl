# -*- coding: utf-8 -*-
'''
目标：尝试使用pyquery，解析https://pythonhosted.org/pyquery/

时间：18-4-16 15：00
作者：yjw

V：1.0
'''

from pyquery import PyQuery as pq
from lxml import etree
import requests

url="https://pythonhosted.org/pyquery/"
page=requests.get(url)
page.encoding=page.apparent_encoding
# print(page.text)
doc=pq(page.text)
print(doc('#quickstart > h1').remove('a').text())
