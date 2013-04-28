#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup

import urllib2
import string

#url ='http://sh.meituan.com'
#response = urllib.request.urlopen(url)
#soup =BeautifulSoup(response)
#soup.find_all('a')
class tuanitem(object):
    href='www.baidu.com'
    title="baidu"
    price=0
    buynum=0
    def printItem(self):
        print '-title:',self.title,'-price:',self.price,'-buynum:',self.buynum,'-href:',self.href


def crawler(url):
#url ='http://sh.meituan.com'
    response = urllib2.urlopen(url)
    html = response.read()
#    print html
    print '============================================================'
    return html
def crawler_ex(url):
#url ='http://sh.meituan.com'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.16 Safari/534.24'}
    request = urllib2.Request(url,headers=headers)
    #request.add_header('User-Agent', 'baiduspider+')
    response = urllib2.urlopen(request)
    html = response.read()
    #    print html
    print '============================================================'
    return html
def beautifulsoupDemo1():
    demoHtml = """
    <html>
    <head>
    <title>
    page title-luxin
    </title>
    </head>
    <body>
    <p id="firstpara" align="center">
    this is paragraph <b> one </b>
    </p>
    <p id="secondpara" align="blah">
    this is paragraph <b> two </b> <b> two2</b>
    </p>
    </body>
    </html>
    """;
    soup = BeautifulSoup(demoHtml);
    print soup.prettify()
    p=soup('p')
    print soup('p')
    print len(soup('p'))
    print "-----",p[0],"---------"
    print "-----",p[1],"---------"
    print soup.html.head.title
    print "======",soup.html.head.title.string,"======"
    print soup.html.body.p

    print "======",soup.findAll('p',align="center"),"======"
    print "==22====",soup.findAll('p',id="firstpara"),"===22==="
    print "==33====",soup('p',align="center")[0]['id'],"===33==="
    print "==44====",soup('p',align="center")[0]['id'],"===33==="
    print "==55====",soup('p')[0].b.string,"===55==="
    print "==66====",soup('p')[1].b.string,"===66==="
    print "==666====",soup('p')[1].b.string,"===6666==="
    firstPTag,secondPTag=soup.findAll('p')
    print firstPTag['id']
    print secondPTag['id']
    print firstPTag.contents
    print "==77====",soup.head.parent.name,"===77==="
    print "==88====",soup.head.parent.parent.__class__.__name__,"===88==="
    p=soup.p
    print p.contents
    print p.contents[0]  #this is the "this is paragraph"
    print p.contents[1]
    print "--------------------"
    print p.contents[1].contents
    # print p.contents[0].contents
    print "==99====",soup.p,"===99==="
    print "==99====",soup.p.nextSibling,"===99==="
    print "))))))))))))))))))))))))))))))))"
    secondBtag=soup.findAll('b')[1]
    print secondBtag
    print secondBtag.previousSibling
    print "(((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))"
    secondPtag=soup.findAll('p')
    print secondPtag[0]
    print secondPtag[1]
    for pp in secondPtag:
        print pp
        for pp in secondPtag:
            print pp

    print "==55====",soup('p')[0].b.string,"===55==="
    print "==66====",soup('p')[1].b,"===66==="
    print "==666====",soup('p')[1].b.string,"===6666==="
    print "==66====",soup('p')[1].b.nextSibling,"===66==="
    print "==22====",soup.findAll('p',id="firstpara").findAll('b'),"===22==="
def html_parser_baidu(html):
    soup = BeautifulSoup(html);
    print "soup=",soup;
    print '============================================================'
    print "==33====",soup('p',id="nv"),"===33==="
    print "==44====",soup('p',id="nv")[0].a,"===44==="
    print "==441====",soup('p',id="nv")[0].b.contents[0],"===44==="
    print "==442====",soup('p',id="nv")[0].a['href'],"===44==="
    # print "==55====",soup('p',id="nv")[0].a.nextSibling,"===55==="
    print "==44====",soup('p',id="nv")[0].findAll('a'),"===44==="
    print '============================================================'
    aa=soup('p',id='nv')[0].findAll('a')
    for at in aa:
        print at
        print at.contents[0]
        print at['href']

    print "---------------------------------"

def html_parser_dianping(html):
    soup = BeautifulSoup(html);
  #  print "soup=",soup;
    print '============================================================'
    print "==33====",soup('li',{"class":"J_dealbox"}),"===33==="
    print '========================888888888888888888===================================='
    itemlist=soup('li',{"class":"J_dealbox"})
    print len(itemlist)
   # itemlist=soup('div',id="content")[0].findAll('div')
    # class=item   会包括class=item odd
   # itemlist=soup('div',{"class":"item"})
   # print len(itemlist)
   # print itemlist[1]
   # item2class(itemlist[1])
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
#beautifulsoupDemo()
    dianping_html=crawler("http://t.dianping.com/shanghai")
    html_parser_dianping(dianping_html)
#    beautifulsoupDemo1()
    print "end....."
    print "----"
    print "222"
    print "kan push"
