# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline(object):
    def open_spider(self,spider):
        self.f=open('douban.txt','w',encoding='utf-8')
    def close_spider(self,spider):
        self.f.close()
    def process_item(self,item,spider):
        try:
            line = str(item)+'\n'
            self.f.write(line)
        except:
            pass
        return item