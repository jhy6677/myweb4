# -*- coding: utf-8 -*-
import scrapy

import re
from ..items import QtpjtItem
from scrapy.http import Request

class QtspdSpider(scrapy.Spider):
    name = 'qtspd'
    allowed_domains = ['58pic.com']
    start_urls = ('http://www.58pic.com/tb/',)

    def parse(self, response):
        item = QtpjtItem()
        paturl = "(http://pic.qiantucdn.com/58pic/.*?).jpg"
        item["picurl"] = re.compile(paturl).findall(str(response.body))
        patlocal = "http://pic.qiantucdn.com/58pic/.*?/.*?/.*?/(.*?).jpg"
        item["picid"] = re.compile(patlocal).findall(str(response.body))
        yield item
        for i in range(1,201):
            nexturl = "http://www.58pic.com/tb/id-"+str(i)+".html"
            yield Request(nexturl,callback=self.parse)
