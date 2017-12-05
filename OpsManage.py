# coding:utf-8
import sqlite3
import os

message = str(input("plese input something:"))
connect = sqlite3.connect('applist.db')
cursor = connect.cursor()


def selectdata():
    values = cursor.execute('select * from app where appname = ' + "'" + message + "'")
    for row in values:
        print("id ", row[0])
        print("department", row[1])
        print("appname", row[2])
    print("信息已查出.")
    cursor.close()
    connect.close()


selectdata()
