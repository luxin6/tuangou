from bs4 import BeautifulSoup

import urllib2

#url ='http://sh.meituan.com'
#response = urllib.request.urlopen(url)
#soup =BeautifulSoup(response)
#soup.find_all('a')

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
def beautifulsoupDemo():
    demoHtml = """
    <html>
    <body>
    <div class="icon_col">
    <h1 class="h1user">crifan</h1>
    </div>
    </body>
    </html>
    """;
    soup = BeautifulSoup(demoHtml);
    print "type(soup)=",type(soup); #type(soup)= <type 'instance'>
    print "soup=",soup;

    # 1. extract content
    # method 1: no designate para name
    #h1userSoup = soup.find("h1", {"class":"h1user"});
    # method 2: use para name
    h1userSoup = soup.find(name="h1", attrs={"class":"h1user"});

    # more can found at:
    #http://www.crummy.com/software/BeautifulSoup/bs3/documentation.zh.html#find%28name,%20attrs,%20recursive,%20text,%20**kwargs%29
    print "h1userSoup=",h1userSoup; #h1userSoup= <h1 class="h1user">crifan</h1>
    h1userUnicodeStr = h1userSoup.string;
    print "h1userUnicodeStr=",h1userUnicodeStr; #h1userUnicodeStr= crifan

def html_parser(html):
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
def crawler(url):
#url ='http://sh.meituan.com'
    response = urllib2.urlopen(url)
    html = response.read()
    print html
    print '============================================================'
    return html

if __name__ == "__main__":
#beautifulsoupDemo()
    meituan_html=crawler("http://www.baidu.com")
    html_parser(meituan_html)
#    beautifulsoupDemo1()
    print "end....."
