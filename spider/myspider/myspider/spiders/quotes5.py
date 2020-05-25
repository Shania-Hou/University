# -*- coding: utf-8 -*-
import scrapy
from ..items import MyspiderItem_score

from lxml import etree


class Quotes5Spider(scrapy.Spider):
    name = 'quotes5'
    allowed_domains = ['college.gaokao.com']
    # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36", }

    start_urls = []
    for i in range(1, 33, 1):
        url = 'http://college.gaokao.com/schlist/s1/p' + str(i) + '/'
        start_urls.append(url)

    def parse(self, response):
        quotes = response.xpath('//div[@class="scores_List"]/dl ')
        for quote in quotes:
            item = MyspiderItem_score()
            uname = quote.xpath('dt/strong/a/text()').extract()
            if len(uname)!= 0 :
                item['uname'] = uname[0].replace(' ','').replace('\r','').replace('\n','')
                item['uid'] = int(quote.xpath('dt/a/@href').extract()[0].replace('http://college.gaokao.com/school/','').replace('/',''))
                item['sp_type'] = '理科'
                uid = item['uid']
                deep_url = 'http://college.gaokao.com/school/tinfo/'+str(uid)+'/result/20/1/'
                # yield item
                # print (deep_url)
                yield scrapy.Request(deep_url, meta={'item': item}, callback=self.deep_parse)
            else:
                continue


    def deep_parse(self,response):
        item = response.meta['item']
        print("**************************************************************")
        quotes2 = response.xpath('//div[@id="pointbyarea"]/table')
        for quote in quotes2:
            item = response.meta['item']
            year = quote.xpath('tr/td[1]/text()').extract()

            if year!=0:
                item['year'] = int(year[0].replace(' ','').replace('\r','').replace('\n',''))
                item['score'] = int(quote.xpath('tr/td[2]/text()').extract()[0].replace(' ', '').replace('\r', '').replace('\n', ''))

            else:
                continue
        # print(quotes2)
            yield item
