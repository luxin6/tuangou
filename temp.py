from bs4 import BeautifulSoup

soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>')
print soup.p
print soup.p.a['rel']
print soup.p.a.string
print soup.p.a.contents
print soup.p.contents
print soup.p.contents[0]
print soup.p.contents[1]
print soup.p.contents[1].string


a="tt"
b="yyy"+a
print b
