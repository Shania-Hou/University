# import pymysql
# from twisted.enterprise import adbapi
# from scrapy.utils.project import get_project_settings
# import time

# class DBHelper():
#     def __init__(self):
#         settings = get_project_settings()

#         dbparams=dict(
#             host=settings['MYSQL_HOST'],  #读取settings中的配置
#             db=settings['MYSQL_DBNAME'],
#             user=settings['MYSQL_USER'],
#             passwd=settings['MYSQL_PASSWD'],
#             charset='utf8',  #编码要加上，否则可能出现中文乱码问题
#             cursorclass=pymysql.cursors.DictCursor,
#             use_unicode=False,
#         )
#         dbpool=adbapi.ConnectionPool('MySQLdb',**dbparams)#**表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....
#         self.dbpool = dbpool#相当于dbpool付给了这个类，self中可以得到
#     #写入数据库中
#     def _conditional_insert(self,tx,item):
#         #print item['name']
#         sql="insert into university_list(u_name,u_pro,u_type,u_administrattion,if_985,if_211,u_level,u_local,u_id) values(%s,%s,%s,%s,%d,%d,%s,%s,%d)"
#         params=(item["name"],item["url"])
#         tx.execute(sql,params)
#     #错误处理方法
#     def _handle_error(self, failue, item, spider):
#         print(failue)
    