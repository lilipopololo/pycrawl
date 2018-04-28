# -*- coding: utf-8 -*-
'''
目标网址：http://k.360kan.com/pc/list?channel_id=2
目标：快视频下载

时间：3,28 13-16
作者：yjw

V：1.0
'''

import urllib.request
import json
import re

# list_url="http://pc.k.360kan.com/pc/list?n=10&p=2&f=json&ajax=1&uid=e00ec0d075d4a06575ceb1a12746a700&channel_id=2&dl=&callback=jQuery19109390930896809959_1522211260983&_=1522211260986"

page_num = 1
while True:
    list_url = "http://pc.k.360kan.com/pc/list?n=10&p=" + \
        str(page_num) + \
        "&f=json&ajax=1&uid=e00ec0d075d4a06575ceb1a12746a700&channel_id=2&dl="
    # print(urllib.request.urlopen(list_url).read().decode("utf-8"))
    list_data = json.loads(urllib.request.urlopen(
        list_url).read().decode("utf-8"))["data"]["res"]
    for eve_data in list_data:
        # print(eve_data)
        title = eve_data["t"]
        data_id = re.findall('detail/(.*?)\?', eve_data["u"])[0]
        data_url = "http://pc.k.360kan.com/pc/play?id=" + data_id
        file_url = json.loads(urllib.request.urlopen(
            data_url).read().decode('utf-8'))["data"]["url"]
        # print(file_url)
        try:
            with open(title + ".mp4", "wb") as f:
                f.write(urllib.request.urlopen(file_url).read.decode("urf-8"))
                print(title)
        except:
            pass
        if len(list_data) > 5:
            page_num = page_num + 1
        else:
            break

    # data_url="http://pc.k.360kan.com/pc/play?callback=jQuery191037915804138054776_1522212801572&id=QroGMZvL1W8G&f=json&ucheck=2b4915550874933c320cf1d2b52f0a4d&uid=e00ec0d075d4a06575ceb1a12746a700&version=&sign=pc&resign=pc&is_recom=1&strategy=2.6.28.18.b82x4463ewqm.8.1lp.13.vny7vk..27.5v0f74ows6xd&channel_id=2&end=pc&is_new_recom=1&userclick=1&dl=&_=1522212801581"
    # data_url="http://pc.k.360kan.com/pc/play?id=QroGMZvL1W8G"
    # print( json.loads(urllib.request.urlopen(data_url).read().decode("utf-8"))["data"]["url"] )
