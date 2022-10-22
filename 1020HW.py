# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 13:17:39 2022

@author: Fang Yu
"""

import dbHW

option = input("請選擇服務項目 (1)新增員工資料 (2)新增工作資料 (3)修改員工資料 (4)查詢員工資料 (5)查詢員工資料及工作內容 : ")

if option == '1':    
    print("新增員工基本資料")
    employeeId = input("請輸入工號: ")
    name = input("請輸入員工姓名: ")
    sex = input("請輸入性別(M/F): ")
    tel = input("請輸入手機號碼: ")
    assume = input("請輸入到職日期(YYYY-MM-DD): ")

    sql = "insert into employee(name,sex,tel,assume) values ('{}','{}','{}','{}','{}')".format(employeeid,name,sex,tel,assume)
    
    cursor = dbHW.conn.cursor()
    cursor.execute(sql)
    dbHW.conn.commit()

elif option == '2':    
    print("請輸入工作內容: ")
    items = input("請輸入工作名稱: ")
    info = input("請敘述工作內容: ")
    employeeid = input("請輸入工號: ")
    
    sql = "insert into works(items,info,employeeid) values ('{}','{}','{}')".format(items,info,employeeid)
    
    cursor = dbHW.conn.cursor()
    cursor.execute(sql)
    dbHW.conn.commit()

elif option == '3':    
    employeeId = input("請輸入工號: ")
    
    sql = "select * from employee where id = '{}'".format(employeeId)
     
    cursor = dbHW.conn.cursor()
    cursor.execute(sql)
    dbHW.conn.commit()
    
    res = cursor.fetchall()
    
    print("員工基本資料")
    for row in res:
        print(row[1])
        print(row[2])
        print(row[3])
    
    employeeId = input("請輸入工號: ")
    sex = input("請更新性別(M/F): ")
    tel = input("請輸入更新手機號碼: ")
    
    sql = "update employee set sex='{}', tel='{}' where id='{}'".format(sex,tel,employeeId)
    
    cursor = dbHW.conn.cursor()
    cursor.execute(sql)
    dbHW.conn.commit()
    
elif option == '4':
    
    employeeId = input("請輸入工號: ")
    
    sql = "select * from employee where id = '{}'".format(employeeId)
     
    cursor = dbHW.conn.cursor()
    cursor.execute(sql)
    dbHW.conn.commit()
    
    res = cursor.fetchall()
    
    print("員工基本資料")
    for row in res:
        print("工號: ",row[0])
        print("姓名: ",row[1])
        print("性別: ",row[2])
        print("手機: ",row[3])
        print("到職日: ",row[4])

elif option == '5':
    employeeId = input("請輸入工號: ")
    
    sql = "select * from employee where id = '{}'".format(employeeId)
    
    cursor = dbHW.conn.cursor()
    cursor.execute(sql)
    dbHW.conn.commit()
    res = cursor.fetchall()
    
    print("員工基本資料")
    for row in res:
        print("姓名: ",row[1])

    
    
    sql = "select * from works where employeeid='{}'".format(employeeId)     
    cursor = dbHW.conn.cursor()
    cursor.execute(sql)
    dbHW.conn.commit()
    
    resWork = cursor.fetchall()
    
    for row in resWork:
        print("工作名稱: ",row[1])
        print("工作內容: ",row[2])

else:
    print("請選擇有效項目")    

dbHW.conn.close()
