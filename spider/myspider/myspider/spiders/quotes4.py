# -*- coding: utf-8 -*-
import scrapy
from ..items import MyspiderItem_speciality

class Quotes3Spider(scrapy.Spider):
    name = 'quotes4'
    allowed_domains = ['zuihaodaxue.com']
    start_urls = ['https://gaokao.chsi.com.cn/sch/zyk/zydm_bk.jsp']


    def parse(self, response):
        
        
        quotes = response.xpath('//div[@class="left"]/table/tbody')
        print ("-------------------start--------------------")
        for quote in quotes:
            print ("11111111111111111111111111111111111")
            item = MyspiderItem_speciality() 

            item['sp_id'] = quote.xpath('tr/td').extract()
                #爬取2017年的
            # item['sp_dep'] = quote.xpath('td[3]/text()').extract()[0].replace(' ','').replace('\r','').replace('\n','')
           
            #     #爬取2018/2019
            # item['sp_smallDep'] = quote.xpath('td[4]/text()').extract()[0].replace(' ','').replace('\r','').replace('\n','')
            # item['sp_name'] = quote.xpath('td[4]/text()').extract()[0].replace(' ','').replace('\r','').replace('\n','')
            
            yield item

        
        print ("-------------------end--------------------")

