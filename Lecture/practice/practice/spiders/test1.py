# -*- coding: utf-8 -*-
import scrapy


class Test1Spider(scrapy.Spider):
    name = 'test1'
    allowed_domains = ['www.naver.com'] ## 이 주소만 크롤링 선언 // 필수 X 옵션 O
    start_urls = ['http://www.naver.com/','http://www.daum.net'] # 리스트 형태 : 여러가지 주소 가능 

    def parse(self, response):
        print(response.url)
