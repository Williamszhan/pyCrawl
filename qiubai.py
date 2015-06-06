# -*- coding: utf-8 -*-
__author__ = 'coral'
import os
import urllib
import urllib2
import re
import string
import sys

class Spider:

    def __init__(self):
        self.page = 1


    def GetPage(self,page):
        url ='http://m.qiushibaike.com/textnew/page/'+str(page)
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent':user_agent}
        req = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(req)
        # page = response.read().decode('utf-8')
        pageContent = response.read()
        items = re.findall('<div class="content">\n\n(.*?)<!--(.*?)-->\n\n</div>',pageContent,re.S)
        itemCollection = []
        for item in items:
            itemCollection.append([item[1],item[0].replace("<br/>","\n")])
            print u"时间:",item[1],"\n", item[0].replace("<br/>","\n")
        SaveText(page,itemCollection)
        return itemCollection

def SaveText(page,msg):
    # 1页存一个txt
    # if os.path.exists(str(page)+".txt"):
    #     print "Error:%s already exists" % str(page)+".txt"
    if not os.path.exists(".\\notes"):
        os.mkdir(".\\notes")
    file = open(".\\notes\\"+str(page)+".txt",'w')
    file.writelines(['日期:%s\n%s\n' %(x[0],x[1]) for x in msg])
    file.close()

Model = Spider()
for i in range(1,35):
    Model.GetPage(i)