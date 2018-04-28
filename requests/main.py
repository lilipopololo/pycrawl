# import requests
# r=requests.get('http://www.baidu.com')
# if r.raise_for_status():
#     print r.encoding#header猜测
#     print(r.apparent_encoding)#从内容猜测
#     r.encoding='utf-8'
#     print(r.text)
import requests
from bs4 import BeautifulSoup

def getHTMLText(url, ua, kw):
    try:
        r = requests.get(url, headers=ua, params=kw)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '产生异常'


if __name__ == '__main__':
    url = 'http://www.baidu.com'  # baidu search engine
    # url = input('please input url:')
    ua = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
                        'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                        'Chrome/65.0.3325.146 Safari/537.36'}
    kw = {'wd': 'python'}
    print(url + '\n' + str(ua))
    demo=getHTMLText(url, ua, kw)
    #print(demo)
    soup=BeautifulSoup(demo,"lxml")
    title=soup.title
    tag=soup.a
    html=soup.prettify()
    print(tag)