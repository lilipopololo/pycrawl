import urllib.request
import re


# 打开网页
def url_open(url):
    header = ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) "
                            "AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
    opener = urllib.request.build_opener()
    opener.addheader = [header]
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
    return data


# 获取自拍栏目总的页面书
def get_num(url):
    data = url_open(url)
    pat = "span aria-current=\"page\" class=\"page-numbers current\">(.+?)"
    num = re.compile(pat).findall(data)[-1]
    return num


if __name__ == '__main__':
    try:
        # 爬取的页面地址
        url = "http://www.mzitu.com/zipai/"
        num = get_num(url)
        for i in range(1, int(num) + 1):
            # 自拍每一个页面的地址
            page_url = "http://www.mzitu.com/zipai/comment-page-" + str(i)
            # 图片的匹配
            img_pat = '<p><img src="(.+?)"'
            data = url_open(page_url)
            img_list = re.compile(img_pat).findall(str(data))
            for j in range(len(img_list)):
                img_url = img_list[j]
                img = "D:/" + str(i) + " " + str(j) + ".jpg"
                print("正在下载第" + str(i) + "页，第" + str(j) + "个图片")
                urllib.request.urlretrieve(img_url, img)
                print("第" + str(i) + "页，第" + str(j) + "个图片下载完成")
                urllib.request.urlcleanup()  # 清理缓存
    except Exception as e:
        print(e)

# num_pat = "<span aria-current=\"page\" class=\"page-numbers current\">(.+?)"
# page_url = "http://www.mzitu.com/zipai/comment-page-" + str(i)
# img_pat = '<p><img src="(.+?)"'
