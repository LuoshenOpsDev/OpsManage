# coding:utf-8
import sqlite3
import json

message = str(input("plese input something:"))
connect = sqlite3.connect('applist.db')
cursor = connect.cursor()


def selectdata():
    cursor.execute('select * from app where appname = ' + "'" + message + "'")
    value = cursor.fetchall()
    jsonDataraw = []
    for row in value:
        result = {}
        result['id'] = row[0]
        result['department'] = row[1]
        result['appname'] = row[2]
        result['ip'] = row[3]
        result['instance'] = row[4]
        result['port'] = row[5]
        result['memery'] = row[6]
        result['type'] = row[7]
        jsonDataraw.append(result)
    jsondata = json.dumps(jsonDataraw, ensure_ascii=False)
    print(jsondata[1:len(jsondata) - 1])

    print("信息已查出.")
    cursor.close()
    connect.close()

selectdata()
