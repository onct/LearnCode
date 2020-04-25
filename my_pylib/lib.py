import re
import requests
from selenium import webdriver
from time import sleep
# get html

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36 Edg/83.0.461.1'
}


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encodingF
        return r.text # r.json()
    except:
        return ""


# get post session
#session = requests.Session()
# data = {
    # 'username': 'name',
   # 'password': 'password'}
#r = session.post('url', data)
#r = session.get('url')


# download with stream
def download(requests, url, file_path):
    r = requests.get(url, stream=True)
    with open('filename', 'wb') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)


# webdriver chrome
driver = webdriver.Chrome()
print(driver.get('https://www.wenjuan.top/s/NJ3EvuS'))
# webdriver for edge need let driver to edge(chrouim) file folder
driver = webdriver.Edge(
    r"C:\Program Files (x86)\Microsoft\Edge Dev\Application\msedgedriver.exe")
print(driver.get('https://www.wenjuan.top/s/NJ3EvuS'))

# #scrapy shell
# 1.scrapy startproject name
# 2.scrapy genspider name domain
# 3.scrapy genspider -t crawl name domain