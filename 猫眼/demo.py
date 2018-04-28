# -*- coding: utf-8 -*-
'''
目标：http://maoyan.com

时间：18-4-16
作者：yjw

V：1.0
'''
from pyquery import PyQuery as pq
import requests
from requests.exceptions import RequestException


def get_one_page(url):
    try:
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
        res = requests.get(url,headers=headers)
        if(res.status_code == 200):
            # res.encoding=res.apparent_encoding
            return res.text
        return None
    except RequestException:
        return None

def 

def main():
    url = "http://maoyan.com/board"
    print(get_one_page(url))


if __name__ == "__main__":
    main()
