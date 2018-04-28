import requests
url="http://m.ip138.com/ip.asp?ip="
try:
    r=requests.get(url+"42.185.148.121")
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text)
except:
    print('失败')
