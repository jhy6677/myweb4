# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest

class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/user/profile']

    def parse(self, response):
        keys = response.css('table label::text').re('(.+):')
        values = response.css('table td.w2p_fw::text').extract()

        yield dict(zip(keys,values))


    log_url = 'http://http://example.webscraping.com/user/login'

    def start_requests(self):
            yield Request(self.log_url,callback=self.login)


    def login(self,response):
        fd = {'email':'925611923@qq.com','password':'12345678'}
        yield FormRequest.from_response(response,formdata=fd,callback=self.parse_login)

    def parse_login(self,response):
        if'Welcome Jia' in response.text:
            yield from super().start_requests()