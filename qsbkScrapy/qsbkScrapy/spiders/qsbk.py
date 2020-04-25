 # -*- coding: utf-8 -*-
import scrapy
from qsbkScrapy.items import QsbkscrapyItem

class QsbkSpider(scrapy.Spider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    base_domain = 'https://www.qiushibaike.com'

    def parse(self, response):
        results = response.xpath("//div[@class='col1 old-style-col1']/div")
        for result in results:
            author=result.xpath(".//h2/text()").get()
            content = result.xpath(".//div[@class='content']//text()").getall()
            content = "".join(content).strip()
            item = QsbkscrapyItem(author = author,content=content)
            yield item
        next_url = response.xpath("//div[@class='col1 old-style-col1']/ul[@class='pagination']/li[last()]/a/@href").get()
        # print('='*5)
        # print(next_url)
        if not next_url:
            return 
        else:
            yield scrapy.Request(self.base_domain+next_url,callback=self.parse)

        
