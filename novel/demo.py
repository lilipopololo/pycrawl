import requests

url="https://www.xxbiquge.com/77_77268/336802.html"
# url="http://top.17k.com/"
headers={  
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}
r=requests.get(url,headers=headers)
r.raise_for_status()
r.encoding=r.apparent_encoding
print(r.text)

