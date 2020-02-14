#-*-coding：utf-8-*-
#coding=utf-8
"""
Created on Thu Feb 13 14:59:17 2020

@author: goatbishop
"""

import pymysql
db = pymysql.connect(host = '127.0.0.1',
                     port = 3306,
                     user = 'root',
                     passwd = '19970928',
                     database = 'stu',
                     charset = 'utf8')
#获取游标对象
cur = db.cursor()

for i in range(1,4):
    image_name = 'IMG%d.jpg' % i
    image_path = 'image/%s' % image_name
    with open(image_path, "rb") as fd:
        data = fd.read()
    
    try:
        sql = "insert into Images \
        values(%s, %s,%s, %s);"
        
        cur.execute(sql, [str(i), image_name, image_path, data])
        db.commit()
    except Exception as e:
        db.rollback()
        print("错误信息: ",e)

cur.close()
db.close()
    
        