# -*- coding: utf-8 -*-
import scrapy
from ecommerce.items import EcommerceItem # ecommerce 폴더에 item class 소환

class GmarketSpider(scrapy.Spider):
    name = 'gMarket'
    allowed_domains = ['corners.gmarket.co.kr/Bestsellers']
    start_urls = ['http://corners.gmarket.co.kr/Bestsellers/']

    def parse(self, response):
        titles = response.css(
            'div.best-list li > a::text').getall()
        prices = response.css(
            'div.best-list ul li div.item_price div.s-price strong span::text').getall()
        for num, title in enumerate(titles):
            item = EcommerceItem()
            item['title'] = title #'title'은 items.py 의 변수
            item['price']= prices[num]
            yield item  # item 쌓는다(?)
