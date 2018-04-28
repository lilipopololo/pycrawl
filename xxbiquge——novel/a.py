# coding:utf-8


from pyquery import PyQuery as pq
import requests
import os

def input(content):
    with open("剑来.txt", "a",encoding="utf-8") as f:
        f.write(content)

base_url = "https://www.xxbiquge.com"
start_url = "https://www.xxbiquge.com/77_77268/"

res = requests.get(start_url)
res.encoding = res.apparent_encoding
query = pq(res.text)
text_list = [{"name":pq(eve_ch).text(),"url":base_url+pq(eve_ch).attr("href")} for eve_ch in query("#list a")]

#print(text_list)
try:
    os.mkdir("./剑来")
except FileExistsError:
    pass
os.chdir("./剑来")

for info in text_list:
    branch=requests.get(info["url"])
    branch.encoding=branch.apparent_encoding
    d=pq(branch.text)
    title=pq(d(".bookname h1")).text()
    
    para=pq(d("#content")).text()
    input(title+"\n"+para+"\n")
    print(title+"写入")



