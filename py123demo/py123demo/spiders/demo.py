# -*- coding: utf-8 -*-
import scrapy
import re

class DemoSpider(scrapy.Spider):
    name = 'demo'
    # allowed_domains = ['python123.io']
    start_urls = ['http://python123.io/ws/demo.html']

    def parse(self, response):
        for href in response.css('a::attr(href)').extract():
            try:
                demo = re.findall(r"[s][hz]\d{6}",href)[0]
                url =''+demo+'.html'
                yield scrapy.Request(url,callback=self.parse_demo)
            except:
                continue
        """fname = response.url.split('/')[-1]
        with open(fname, "wb") as f:
            f.write(response.body)
        self.log('saved file %s.' % name)"""
    def parse_demo(self,response):
        infodict={}
        demoInfo=response.css('.demo.class')
        name = demoInfo.css('.div-name').extract()
        keyList=demoInfo.css('<>').extract()
        valueList=demoInfo.css('<>').extract()
        for i in range(keyList):
            key = re.findall(r'>.*</tag>',keyList[i])[0][1:-5]
            try:
                value = re.findall(r'>.*</tag>',valueList[i])[0][0:-5]
            except:
                value='--'
            infodictp[key]=value
        infodict.update(
            {'name' :re.findall()}
        )

