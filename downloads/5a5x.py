import requests
from lxml import etree
import os



list_data=["etools","eimage","emedia","egame","edata","ecom","enetwork"]
for eve_list_data in list_data:
    os.mkdir("./"+eve_list_data)
    os.chdir("./"+eve_list_data)
    base_url = "http://www.5a5x.com/wode_source/"+eve_list_data
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
    }
    base_source = requests.get(base_url, headers=headers).content
    base_HTML = etree.HTML(base_source)
    base_total = int(base_HTML.xpath(
        "//*[@id='pages']/b[2]/text()")[0].replace("/", ""))
    print(base_total)
    for eve_page_list in range(1,base_total+1):
        print("http://www.5a5x.com/wode_source/etools/"+str(eve_page_list)+".html")
        page_HTML=etree.HTML(requests.get("http://www.5a5x.com/wode_source/etools/"+str(eve_page_list)+".html", headers=headers).content)
        content_list = page_HTML.xpath("//dl/dt/a/@href")
        for eve_content in content_list:
            content_url = "http://www.5a5x.com/" + eve_content
            content_source = requests.get(content_url, headers=headers).content
            content_HTML = etree.HTML(content_source)
            content_title = content_HTML.xpath("//caption/span/text()")[0]
            content_download = "http://www.5a5x.com/" + \
                content_HTML.xpath("//*[@id='down_address']/a/@href")[0]
            download_source = requests.get(content_download, headers=headers).content
            download_HTML = etree.HTML(download_source)
            download_url = "http://www.5a5x.com/" + download_HTML.xpath('//a/@href')[0]
            print(download_url)
            with open(content_title + ".zip", "wb") as f:
                f.write(requests.get(download_url, headers=headers).content)
    os.chdir("../")