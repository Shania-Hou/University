# from myspider.db.dbhelper import DBHelper
import pymysql
#定义数据管道
class MyspiderPipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlPipeline_ulist(object):
    # open_spider()和close_spider()：只在爬虫被打开和关闭时，执行一次。
    def open_spider(self, spider):
        self.connect = pymysql.connect(
            host='localhost',
            user='root',
            port=3306,
            passwd='',
            db='university',
            charset='utf8'
        )
        self.cursor = self.connect.cursor()

    def process_item(self,item,spider):
        # 2015年大学排序表
        # insert_sql = "INSERT INTO list_2015(ranking,uname) VALUES (%s, %s)"
        # 2016年大学排序表
        # insert_sql = "INSERT INTO list_2016(ranking,uname) VALUES (%s, %s)"
        # 2017年大学排序表
        # insert_sql = "INSERT INTO list_2017(ranking,uname) VALUES (%s, %s)"
        # 2018年大学排序表
        # insert_sql = "INSERT INTO list_2018(ranking,uname) VALUES (%s, %s)"
        # 2019年大学排序表
        insert_sql = "INSERT INTO ulist_year(ranking,uname,u_year) VALUES (%s, %s,2019)"

        self.cursor.execute(insert_sql, (item['ranking'], item['uname']))
        self.connect.commit()


    def close_spider(self,spider):
        print('----------关闭数据库资源-----------')
        self.cursor.close()
        self.connect.close()



class MysqlPipeline_university(object):
    # open_spider()和close_spider()：只在爬虫被打开和关闭时，执行一次。
    def open_spider(self, spider):
        self.connect = pymysql.connect(
            host='localhost',
            user='root',
            port=3306,
            passwd='',
            db='university',
            charset='utf8'
        )
        self.cursor = self.connect.cursor()

    def process_item(self,item,spider):
        insert_sql = "INSERT INTO university(u_id,u_name,u_pro,u_type,u_administration,if985,if211,u_level,u_local,u_url,u_phone) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        self.cursor.execute(insert_sql, (item['u_id'], item['u_name'],item['u_pro'], item['u_type'],item['u_administration'], item['if985'],item['if211'], item['u_level'],item['u_local'],item['u_url'],item['u_phone'],))
        self.connect.commit()


    def close_spider(self,spider):
        print('----------关闭数据库资源-----------')
        self.cursor.close()
        self.connect.close()



class MysqlPipeline_splist(object):
    # open_spider()和close_spider()：只在爬虫被打开和关闭时，执行一次。
    def open_spider(self, spider):
        self.connect = pymysql.connect(
            host='localhost',
            user='root',
            port=3306,
            passwd='',
            db='university',
            charset='utf8'
        )
        self.cursor = self.connect.cursor()

    def process_item(self,item,spider):
        insert_sql = "INSERT INTO splist_year(sp_year,ranking,sp_name,u_name) VALUES (%s,%s,%s,%s)"

        self.cursor.execute(insert_sql, (item['sp_year'], item['ranking'],item['sp_name'], item['u_name']))
        self.connect.commit()


    def close_spider(self,spider):
        print('----------关闭数据库资源-----------')
        self.cursor.close()
        self.connect.close()



class MysqlPipeline_score(object):
    # open_spider()和close_spider()：只在爬虫被打开和关闭时，执行一次。
    def open_spider(self, spider):
        self.connect = pymysql.connect(
            host='localhost',
            user='root',
            port=3306,
            passwd='',
            db='university',
            charset='utf8'
        )
        self.cursor = self.connect.cursor()

    def process_item(self,item,spider):
        insert_sql = "INSERT INTO pro_scoreline(sp_type,year,score,uname) VALUES (%s,%s,%s,%s)"

        self.cursor.execute(insert_sql, (item['sp_type'], item['year'],item['score'], item['uname']))
        self.connect.commit()


    def close_spider(self,spider):
        print('----------关闭数据库资源-----------')
        self.cursor.close()
        self.connect.close()
