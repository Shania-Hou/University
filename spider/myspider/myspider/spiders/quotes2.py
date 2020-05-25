# -*- coding: utf-8 -*-
import scrapy
from ..items import MyspiderItem_uList

from lxml import etree


class Quotes2Spider(scrapy.Spider):
    name = 'quotes2'
    allowed_domains = ['zuihaodaxue.com']
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 OPR/57.0.3098.116", }
    # start_urls = ['http://www.zuihaodaxue.com/zuihaodaxuepaiming2015_0.html']
    # start_urls = ['http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html']
    # start_urls = ['http://www.zuihaodaxue.com/zuihaodaxuepaiming2017.html']
    # start_urls = ['http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html']
    start_urls = ['http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html']

    def parse(self, response):
        quotes = response.xpath('//div[@class="news-text"]/table/tbody/tr')
        print ("-------------------start--------------------")
        for quote in quotes:
            item = MyspiderItem_uList() 
            item['ranking'] = int(quote.xpath('td[1]/text()').extract()[0].replace(' ','').replace('\r','').replace('\n',''))
            item['uname'] = quote.xpath('td[2]/div/text()').extract()[0].replace(' ','').replace('\r','').replace('\n','')

            yield item
        print ("-------------------end--------------------")

