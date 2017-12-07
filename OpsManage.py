# coding:utf-8
import sqlite3
import json

message = str(input("plese input something:"))
connect = sqlite3.connect('applist.db')
cursor = connect.cursor()


def selectdata():
    cursor.execute('select * from app where appname = ' + "'" + message + "'")
    value = cursor.fetchall()
    jsondataraw = []
    for row in value:
        result = {'id': row[0], 'department': row[1], 'appname': row[2], 'ip': row[3],
                  'instance': row[4], 'port': 'row[5]', 'memery': row[6], 'type': row[7]}
        jsondataraw.append(result)
    jsondata = json.dumps(jsondataraw, ensure_ascii=False)
    print(jsondata[1:len(jsondata) - 1])

    print("信息已查出.")
    cursor.close()
    connect.close()


selectdata()
