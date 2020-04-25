# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    movie_name = scrapy.Field()
    movie_director = scrapy.Field()
    movie_writer = scrapy.Field()
    movie_actor = scrapy.Field()
    movie_type = scrapy.Field()
    movie_time = scrapy.Field()
    movie_runtime = scrapy.Field()
    movie_grade = scrapy.Field()
    movie_summary = scrapy.Field()

