import pymysql
from flask import Flask,render_template,url_for
import json

app = Flask(__name__)


@app.route("/")
# def my_tem():
#     # 在浏览器上渲染my_templaces.html模板
#     return render_template('university_detail.html')

@app.route('/test',methods=['POST'])
def myTest():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 passwd='',
                                 db='university',
                                 port=3306,
                                 charset='utf8'
                                 )
    cur=connection.cursor() #游标（指针）cursor的方式操作数据
    sql='select ranking,u_year from ulist_year where uname="北京大学"' #sql语句
    cur.execute(sql) #execute(query, args):执行单条sql语句。
    see=cur.fetchall() #使结果全部可看
    #print(sql)
   #print(see)
    #print(cur)
    #创建json数据
    xdays=[]
    jsonData={}
    yvalues=[]

    for data in see:
        xdays.append(data[0])
        yvalues.append(data[1])

    # print(xdays)
    # print(yvalues)

    jsonData['xdays']=xdays
    jsonData['yvalues']=yvalues

    # print(jsonData)
    #将json格式转成str，因为如果直接将dict类型的数据写入json会发生报错，因此将数据写入时需要用到该函数。
    
    j=json.dumps(jsonData,ensure_ascii=False)
    # print(j)
    cur.close()
    connection.close()
    #渲染html模板
    return (j)

if __name__ == "__main__":
    app.debug = False
    app.run(host='localhost',port=5000)