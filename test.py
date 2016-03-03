#coding=utf-8
import sys
import urllib2
import re
import os
import db.python_mysql_con


from bs4 import BeautifulSoup
import sys
print sys.getdefaultencoding()


# conn,cur = db.python_mysql_con.getConn()
# sql = "insert into newsinfo(id,title, description, link, updated) values (451, 'sad', 'asd', 'asdf', '2016-03-03 05:17:39');"
# print sql
# b = cur.execute(sql)
# conn.commit()
# print b
# print conn.insert_id()
content = urllib2.urlopen('http://news.qq.com').read().decode("gb2312", 'ignore').encode("utf-8")
print content


s = '<title>Ï£À­ÀïÌØÀÊÆÕÖÜ¶þºáÉ¨È«ÃÀ ÌØÀÊÆÕ±»ºÚµô·çÏÕ´ó_ÐÂÎÅ_ÌÚÑ¶Íø</title>'
soup = BeautifulSoup(s, "lxml")
print soup.title.string
def filter_tags(htmlstr):

    # re_title = re.compile('<\s*title[^>]*>[^<]*<\s*/\s*title\s*>', re.I) #去掉title
    re_title = re.compile('<title>*<//title>', re.I) #去掉title

    s=re_title.sub('',htmlstr) #去掉title
    return s


print filter_tags(s)