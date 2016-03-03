#coding=utf-8
import sys
import urllib2
import re
import os
import db.python_mysql_con
from bs4 import BeautifulSoup
# print db.python_mysql_con.getConn()

####################本文件中不能使用###########################
reload(sys)
sys.setdefaultencoding('utf8')
###########################################################



def extract_url(info):
    rege="http://news.qq.com/a/\d{8}/\d{6}.htm"
    re_url = re.findall(rege, info)
    return re_url

def extract_sub_web_title(sub_web):
    re_key = "<title>.+</title>"
    title = re.findall(re_key,sub_web)
    return title

# def extract_sub_web_content(sub_web):
#     re_key = "<div id=\"Cnt-Main-Article-QQ\".*</div>"
#     content = re.findall(re_key,sub_web)
#     return content


#get news
content = urllib2.urlopen('http://news.qq.com').read()
# contentutf8 = content.decode("gb2312").encode("utf8")
# print content
# f = file('result.txt', 'w')
# f.write(content)
# f.close()

# #get the url
get_url = extract_url(content)
print get_url

# generate file
f = file('result.txt','w')
i = 15            #新闻起始位置，前面几条格式不一致
flag = 30
while True:
    f.write(str(i-14)+"\r\n")
    
    #get the sub web title and content
    sub_web = urllib2.urlopen(get_url[i]).read()
    sub_title = extract_sub_web_title(sub_web)
    sub_url = get_url[i]
    desc = "描述"
    now = '2016-03-03 05:17:39'
    conn, cur = db.python_mysql_con.getConn()

    # sub_content = extract_sub_web_content(sub_web)

    #remove html tag
    if sub_title != [] :
        ############################写入文件#################################
        re_content = sub_title[0] + "\r\n"
        # re_content = filter_tags(sub_title[0]+"\r\n"+sub_content[0])
        f.write(re_content.decode("gb2312").encode("utf-8"))
        f.write("\r\n")
        ############################写入文件-END#############################
        #
        ############################写入数据库################################
        print sub_title[0]
        soup = BeautifulSoup(sub_title[0], "lxml")
        print soup.title.string
        sql = """
        insert into newsinfo(title, description, link, updated) values('%s', '%s', '%s', '%s')
        """ % (soup.title.string.decode("gb2312", 'ignore').encode("utf-8"), desc, sub_url, now)
        try:
            a = cur.execute(sql)
            conn.commit()
            print a
        except Exception,e:
            print "System error:", e
        ############################写入数据库END#############################
    else:
        flag = flag +1
    
    if i == flag:
        break
 
    i = i + 1
    print "Have finished %d news" %(i-15)
f.close()
# conn.close()