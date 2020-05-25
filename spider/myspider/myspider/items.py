#定义爬取的数据结构
import scrapy

class MyspiderItem_university(scrapy.Item):
    u_name = scrapy.Field()
    u_local = scrapy.Field()
    u_pro = scrapy.Field()
    u_administration = scrapy.Field()
    u_type = scrapy.Field()
    if985 = scrapy.Field()
    if211 = scrapy.Field()
    u_level = scrapy.Field()
    u_id = scrapy.Field()
    u_url = scrapy.Field()
    u_phone = scrapy.Field()

class MyspiderItem_uList(scrapy.Item):
    ranking = scrapy.Field()
    uname = scrapy.Field()
    u_year = scrapy.Field()


class MyspiderItem_specialityList(scrapy.Item):
    sp_year = scrapy.Field()
    ranking = scrapy.Field()
    sp_dep = scrapy.Field()
    sp_name = scrapy.Field()
    u_name = scrapy.Field()

class MyspiderItem_speciality(scrapy.Item):
    sp_id = scrapy.Field()
    sp_dep = scrapy.Field()
    sp_smallDep = scrapy.Field()
    sp_name = scrapy.Field()


class MyspiderItem_score(scrapy.Item):
    uname = scrapy.Field()
    uid = scrapy.Field()
    sp_type = scrapy.Field()
    score = scrapy.Field()
    year = scrapy.Field()

class MyspiderItem_major(scrapy.Item):
    dep = scrapy.Field()
    sp_class = scrapy.Field()
    sp_name = scrapy.Field()
    alt = scrapy.Field()
