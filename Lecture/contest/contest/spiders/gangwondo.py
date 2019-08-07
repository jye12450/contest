# -*- coding: utf-8 -*-
import scrapy


class GangwondoSpider(scrapy.Spider):
    name = 'gangwondo'
    allowed_domains = ['https://search.naver.com/search.naver?date_from=']
    start_urls = ['http://https://search.naver.com/search.naver?date_from=/']

    def parse(self, response):
        pass
