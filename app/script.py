#!/usr/local/bin/python3
from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import datetime
import csv

# HEADLESSブラウザに接続
browser = webdriver.Remote(
    command_executor='http://selenium-hub:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME)

# csvファイル作成用に日付を取得
dt = datetime.datetime.today()
dtstr = dt.strftime("%Y%m%d%H%M%S")
filename = dtstr + '.csv'

# Googleにアクセス
browser.get('https://store.nintendo.co.jp/dl-soft/sale.html?sort=new&page=1')

header = ['name', 'price', 'discount_rate', 'image_url', 'description_url']
items = []

tags = browser.find_elements_by_tag_name('item-card')
for tag in tags:
    item = []
    item.append(tag.get_attribute('name'))
    item.append(tag.get_attribute('price'))
    item.append(tag.get_attribute('discount-rate'))
    item.append(tag.get_attribute('image-url'))
    item.append(tag.get_attribute('url'))
    items.append(item)

# 終了
browser.close()
browser.quit()

# csv書き出し
with open('./data/' + filename, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(items)
