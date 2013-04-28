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

def html_parser_meituan(html):
    soup = BeautifulSoup(html);
  #  print "soup=",soup;
    print '============================================================'
    print "==33====",soup('div',{"class":"item","class":"item odd"}),"===33==="
    print '========================888888888888888888===================================='
   # itemlist=soup('div',id="content")[0].findAll('div')
    # class=item   会包括class=item odd
    itemlist=soup('div',{"class":"item"})
    print len(itemlist)
    print itemlist[1]
    item2class(itemlist[1])

    for item in itemlist:
        item2class(item)


    print "---------------------------------"

def item2class(item):
#    print item.a['href']
#    print item.em.contents[0]
#    print item.findAll('strong',{"class":"num"})[0].string
#    print item.findAll('span',{"class":"xtitle"})[0].string
    item1=tuanitem()
    item1.href=item.a['href']
    item1.price=item.em.contents[0][1:]
    item1.buynum=item.findAll('strong',{"class":"num"})[0].string
    item1.title=item.findAll('span',{"class":"xtitle"})[0].string
    item1.printItem()



if __name__ == "__main__":
#beautifulsoupDemo()
    meituan_html=crawler("http://sh.meituan.com")
    html_parser_meituan(meituan_html)
#    beautifulsoupDemo1()
    print "end....."
