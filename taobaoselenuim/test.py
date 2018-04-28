from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
import re

broswer = webdriver.Chrome()
wait = WebDriverWait(broswer, 10)


def search():
    try:
        broswer.get('https://www.taobao.com/')
        input = wait.until(
            # EC expected_condition class
            EC.presence_of_element_located((By.CSS_SELECTOR, "#q"))
        )
        submit = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#J_TSearchForm > div.search-button > button"))
        )
        input.send_keys('可可粉')
        submit.click()
        total = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.total"))
        )
        print(total.text)
        return total.text
    except TimeoutException:
        return search()


def next_page(page_number):
    try:
        input = wait.until(
            # EC expected_condition class
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > input"))
        )
        submit = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit"))
        )
        input.clear()
        input.send_keys(page_number)
        submit.click()
        wait.until( EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span')))
        get_products()
    except TimeoutException:
        next_page(page_number)

def get_products():
    wait.until(
        EC.presence_of_all_elements_located(  (By.CSS_SELECTOR,'#mainsrp-itemlist .items .item')  )
    )
    html=broswer.page_source
    doc=pq(html)
    items=doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        get_products  =  {
            'image':item.find('.pic .img').attr('src'),
            'price':item.find('.price').text(),
            'deal':item.find('.deal-cnt').text()[:-3],
            'title':item.find('.title').text(),
            'shop':item.find('shop').text(),
            'location':item.find('.location').text()
        }

def main():
    total = search()
    total = int(re.compile('(\d+)').search(total).group(1))
    print(total)
    for i in range(2, total + 1):
        next_page(i)


if __name__ == "__main__":
    main()
