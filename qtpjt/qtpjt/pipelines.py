# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib.request

class QtpjtPipeline(object):
    def process_item(self, item, spider):
        for i in range(0,len(item["picurl"])):
            thispic = item["picurl"][i]
            trueurl = thispic +"_1024.jpg"
            localpath = "D:/tupian/part19/"+item["picid"][i]+".jpg"
            urllib.request.urlretrieve(trueurl,filename=localpath)
        return item
