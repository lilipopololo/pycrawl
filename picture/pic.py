import requests
import os

url = "http://i0.hdslb.com/bfs/archive/bdb288021ff854d3ac618ac8c1eafd300ec9ed9b.png"
root = "D://"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print('文件以保存')
    else:
        print('文件已存在')
except:
    print("爬去失败")
