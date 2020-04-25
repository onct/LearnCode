# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']
    base_domain = "https://movie.douban.com/top250"

    def parse(self, response):
        movie_urls = response.xpath("//div[@class='hd']/a/@href").getall()
        for movie_url in movie_urls:
            yield scrapy.Request(movie_url, callback=self.parse_movie)
        next_url = response.xpath("//span[@class='next']/a/@href").get()
        print('-'*10)
        print(next_url)
        if not next_url:
            return
        else:
            yield scrapy.Request(self.base_domain+next_url, callback=self.parse)

    def parse_movie(self, response):
        movie_name = response.xpath("//h1/span/text()").get()
        movie_director = response.xpath(
            "//span[@class='attrs']/a/text()").get()
        movie_writer = response.xpath(
            "//div[@id='info']/span[2]/span/a/text()").getall()
        movie_actor = response.xpath(
            "//div[@id='info']/span[3]/span/a/text()").getall()
        movie_type = response.xpath(
            "//div[@id='info']/span[@property='v:genre']/text()").getall()
        movie_time = response.xpath(
            "//span[@property='v:initialReleaseDate']/text()").get()
        movie_runtime = response.xpath(
            "//span[@property='v:runtime']/text()").get()
        movie_grade = response.xpath("//strong/text()").get()
        movie_summary = response.xpath(
            "//span[@property='v:summary']/text()").get()
        item = DoubanItem(movie_name=movie_name, movie_director=movie_director,
                          movie_writer=movie_writer, movie_actor=movie_actor, movie_type=movie_type,
                          movie_time=movie_time, movie_runtime=movie_runtime, movie_grade=movie_grade,
                          movie_summary=movie_summary)
        yield item