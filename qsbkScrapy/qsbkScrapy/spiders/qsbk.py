 # -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup

class QsbkSpider(scrapy.Spider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/2/']

    def parse(self, response):
        soup = BeautifulSoup(response)
        
