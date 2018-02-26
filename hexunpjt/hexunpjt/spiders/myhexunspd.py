# -*- coding: utf-8 -*-
import scrapy
import re
import urllib.request
from ..items import HexunpjtItem
from scrapy.http import Request

class MyhexunspdSpider(scrapy.Spider):
    name = 'myhexunspd'
    allowed_domains = ['hexun.com']
    uid = "shihanbingblog"

    def start_requests(self):
        yield Request("http://"+str(self.uid)+".blog.hexun.com/p1/default.html",headers
        ={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"})


    def parse(self, response):
        item = HexunpjtItem()
        item['name'] = response.xpath("//span[@class='ArticleTitleText']/a/text()").extract()
        item['url'] = response.xpath("//span[@class='ArticleTitleText']/a/@href").extract()

        pat1 = '<script type="text/javascript" src="(http://click.tool.hexun.com/.*?)">'
        hcurl = re.compile(pat1).findall(str(response.body))[0]
        headers2 = ("User-Agent",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")
        opener = urllib.request.build_opener()
        opener.addheaders = [headers2]
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(hcurl).read()
        pat2 = "click\d*?','(\d*?)'"
        pat3 = "comment\d*?','(\d*?)'"
        item["hits"] = re.compile(pat2).findall(str(data))
        item["comment"] = re.compile(pat3).findall(str(data))
        yield item

        pat4 = "blog.hexun.com/p(.*?)/"
        data2 = re.compile(pat4).findall(str(response.body))
        if(len(data2) >= 2):
            totalurl = data2[-2]
        else:
            totalurl = 1

        print("一共"+str(totalurl)+"页")
        for i in range(2,int(totalurl)+1):
            nexturl = "http://"+str(self.uid)+".blog.hexun.com/p"+str(i)+"/default.html"
            yield Request(nexturl,callback=self.parse,headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"})
