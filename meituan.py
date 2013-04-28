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

def html_parser_meituan(html):
    soup = BeautifulSoup(html);
    itemlist=soup('div',{"class":"item"})
    print len(itemlist)
    print itemlist[1]
    item2class(itemlist[1])

    for item in itemlist:
        item2class(item)
    print "---------------------------------"

def item2class(item):
    item1=tuanitem()
    item1.href=item.a['href']
    item1.price=item.em.contents[0][1:]
    item1.buynum=item.findAll('strong',{"class":"num"})[0].string
    item1.title=item.findAll('span',{"class":"xtitle"})[0].string
    item1.printItem()

if __name__ == "__main__":
    meituan_html=crawler("http://sh.meituan.com")
    html_parser_meituan(meituan_html)
    print "end....."
