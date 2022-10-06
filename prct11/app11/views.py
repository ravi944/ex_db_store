from django.shortcuts import render,HttpResponse
import mysql.connector as mysql
import xlrd
import os
import pyexcel as p
import pathlib

def index(request):
# # Open database connection
    db = mysql.connect(host="localhost",user="root",password="1234",database="db_of_sample")
 
    cur = db.cursor()
 
    cur.execute("DROP TABLE IF EXISTS EMPLOYEE")
    sql1 = "CREATE TABLE EXCEL_DATA20 ( first char(20) not null, last char(20), loc char(20) )"
    cur.execute(sql1) #table created

    l=list()
    loc = ("D:\\sampl.xlsx")
    ext = os.path.splitext(loc)
    if ext[-1] == ".xlsx":
        p.save_book_as(file_name=str(loc),dest_file_name = 'your-new-file-out.xls')
        a = xlrd.open_workbook("your-new-file-out.xls")
    else:
        a = xlrd.open_workbook(str(loc))
    sheet = a.sheet_by_index(0)
    sheet.cell_value(0,0)
    l=list()
    for i in range(1,sheet.nrows):
        l.append(tuple(sheet.row_values(i)))
    q="insert into excel_data19(first, last,loc )values(%s,%s,%s)"

    cur.executemany(q,l)
    db.commit()
    db.close()

    return HttpResponse(q)


