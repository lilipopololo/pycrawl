# -*- coding: utf-8 -*-
'''
目标：百度识图 http://image.baidu.com

时间：3-30 15：10
作者：yjw

V：1.0
'''
import requests
import json
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}
url = "http://image.baidu.com/pcdutu/a_upload?fr=html5&target=pcSearchImage&needJson=true"
file = {
    'file': open('test.jpg', 'rb')
}
r = requests.post(url,headers=headers,files=file)
# r.encoding = r.apparent_encoding
print( r.text )
temp_data = json.loads( r.text )
ans_url = "http://image.baidu.com/pcdutu?queryImageUrl=" + str(temp_data['url']) + '&querySign' + temp_data['querySign'] +"&fm=home&uptype=upload_pc&result=result_camera"
pagesource = requests.get(url=ans_url,headers=headers).text
print(pagesource)
guessWord = re.findall("\'guessWord\':\'(.*?)\',",pagesource)
term_data = re.findall("\"name\":\"(.*?)\",\"baike\":{\"url\":\"(.*?)\",\"abstract\":\"(.*?)\",",pagesource)
print(guessWord)
print(term_data)
print("上传的图片可能是：",guessWord)
for eve in term_data:
    print(eve[0],eve[1],eve[2])

# print(temp_data)
'''
动漫图
{"errno":0,"url":"http://e.hiphotos.baidu.com/image/%70%69%63/item/d50735fae6cd7b89eace6bf6032442a7d9330e20.jpg","querySign":"331335521,690749856","simid":"20131210,5277390401366719378"}
http://image.baidu.com/pcdutu?queryImageUrl=http%3A%2F%2Fh.hiphotos.baidu.com%2Fimage%2F%2570%2569%2563%2Fitem%2Ffaedab64034f78f070b6cc8675310a55b3191c01.jpg&querySign=331335521%2C690749856&fm=home&uptype=upload_pc&result=result_camera&vs=90eb1dd1bfa08dbbb3d4e7b71a7777c0e45e1b78

'''
