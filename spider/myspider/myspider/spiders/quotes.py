# -*- coding: utf-8 -*-
import scrapy
from ..items import MyspiderItem_university
from lxml import etree

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['gaokao.chsi.com.cn']
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 OPR/57.0.3098.116", }
    start_urls = ['https://gaokao.chsi.com.cn/sch/search.do?searchType=1&start=0']


    def parse(self, response):
        quotes = response.xpath('//div[@class="yxk-table"]/table/tr')
        for quote in quotes:  
            u_name = quote.xpath('td[@class="js-yxk-yxmc"]/a/text()').extract()
            u_type = quote.xpath('td[4]/text()').extract()
            u_administration = quote.xpath('td[3]/text()').extract()
            if985 = quote.xpath('td[6]/text()').extract()
            if211 = quote.xpath('td[7]/text()').extract()
            u_level = quote.xpath('td[5]/text()').extract()
            u_id = quote.xpath('td[@class="js-yxk-yxmc"]/a/@href').extract()
            url_deep = quote.xpath('td[@class="js-yxk-yxmc"]/a/@href').extract()
            u_pro = quote.xpath('td[2]/text()').extract()
            

            item = MyspiderItem_university() 
            if len(u_name) != 0:
                item['u_name'] = u_name[0].replace(' ','').replace('\r','').replace('\n','')
                item['u_pro'] = u_pro[0].replace(' ','').replace('\r','').replace('\n','')
                item['u_type'] = u_type[0].replace(' ','').replace('\r','').replace('\n','')
                item['u_administration'] = u_administration[0].replace(' ','').replace('\r','').replace('\n','')
                item['u_level'] = u_level[0].replace(' ','').replace('\r','').replace('\n','')
                item['u_id'] = int(u_id[0].replace('/sch/schoolInfo--schId-','').replace('.dhtml','')) 
                # item['url'] = url[0].replace(' ','').replace('\r','').replace('\n','')
                if len(if985) == 2:
                    item['if985'] = 1
                else:
                    item['if985'] = 0

                if len(if211) == 2:
                    item['if211'] = 1
                else:
                    item['if211'] = 0
                
                # print ("".join(url_deep))
                url = 'https://gaokao.chsi.com.cn' + ("".join(url_deep)).replace('schoolInfo','schoolInfoMain')
                # print (url)
                yield scrapy.Request(url, meta={'item':item},callback = self.parse_u_detail)
            else:
                continue

        # 多页爬取
        for i in range(20,2780,20):
            url = 'https://gaokao.chsi.com.cn/sch/search.do?searchType=1&start='+str(i)
            yield scrapy.Request(url,callback = self.parse)
       
    def parse_u_detail(self,response):
        
        quotes2 = response.xpath('//div[@class="mid"]')
        for quote in quotes2:   
            item = response.meta['item']
            u_url = quote.xpath('div[1]/span[1]/a/text()').extract()
            item['u_url'] = " ".join(u_url)
            u_phone = quote.xpath('div[1]/span[2]/text()').extract()
            item['u_phone'] = " ".join(u_phone).replace(' ','').replace('\r','').replace('\n','').replace('\xa0','')
            u_local = quote.xpath('div[2]/span/text()').extract()
            item['u_local'] = " ".join(u_local).replace(' ','').replace('\r','').replace('\n','').replace('\xa0','')

            
            yield item
            


        
        
            

     