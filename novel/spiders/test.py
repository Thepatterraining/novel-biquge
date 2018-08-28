# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    # allowed_domains = ['http://www.biquge.com/']
    start_urls = ['http://www.biquge.com/']

    def parse(self, response):
        self.log('返回值')
        self.log(response.body)
        pass
