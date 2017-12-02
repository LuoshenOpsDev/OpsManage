# coding:utf-8
import sqlite3
import os

ip = str(input("plese input something:"))
conn = sqlite3.connect('luoshen.db')
cr = conn.cursor()


def createdata():
    cr.execute('create table user (id varchar(20) primary key, name varchar(20))')


def insertdata():
    cr.execute("insert into user (id, name) values (10,'10.125.48.21');")
    conn.commit()
    conn.close()
    # cr.close()
    print("has been close")


def selectdata():
    values = cr.execute('select * from user where name = ' + "'" + ip +"'")
    for row in values:
        print("id ", row[0])
        print("name", row[1])
    print("信息已查出.")
    conn.close()


# insertdata()
selectdata()
