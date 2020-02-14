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

sql = "select * from Images;"

cur.execute(sql)
for image in cur.fetchall():
    with open('new_image/%s' % image[1],'wb') as fd:
        fd.write(image[3])



cur.close()
db.close()
    
        
