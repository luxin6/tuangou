#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup

import urllib2
import string

class tuanitem(object):
    href='www.baidu.com'
    title="baidu"
    price=0
    buynum=0
    def printItem(self):
        print '-title:',self.title,'-price:',self.price,'-buynum:',self.buynum,'-href:',self.href


def crawler(url):
    response = urllib2.urlopen(url)
    html = response.read()
    print '============================================================'
    return html
def html_parser_dianping(html):
    soup = BeautifulSoup(html);
    itemlist=soup('li',{"class":"J_dealbox"})
    print len(itemlist)
    print itemlist[0]
    print itemlist[0].h2.a['href']
    print itemlist[0].h2.a['title']
    print itemlist[0].findAll('span',{"class":"deal-count J_dealCount"})[0].string
    print itemlist[0].findAll('div',{"class":"Price-font"})[0].div.string[1:]

    item2class_dianping(itemlist[0])
    for item in itemlist:
        item2class_dianping(item)


    print "---------------------------------"

def item2class_dianping(item):
    item1=tuanitem()
    item1.href="t.dianping.com"+item.h2.a['href']
    item1.title=item.h2.a['title']
    item1.buynum=item.findAll('span',{"class":"deal-count J_dealCount"})[0].string
    item1.price=item.findAll('div',{"class":"Price-font"})[0].div.string[1:]
    item1.buynum=string.strip(str(item1.buynum))
    item1.printItem()

if __name__ == "__main__":
    dianping_html=crawler("http://t.dianping.com/shanghai")
    html_parser_dianping(dianping_html)
    print "end....."
    print "----"
    print "yyyyyyyyyy"
