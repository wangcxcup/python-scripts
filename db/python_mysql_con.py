#coding=utf-8

import MySQLdb

def getConn():
    try:
        conn = MySQLdb.connect(host='localhost',user='root',passwd='root',db='spiderdb',port=3306)
        cur = conn.cursor()
        cur.execute('set names utf8')
        conn.commit()
        return conn, cur
        # cur.execute('select * from user')
        # cur.close()
        # conn.close()
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])
