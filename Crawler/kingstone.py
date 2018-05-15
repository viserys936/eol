# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re
r = requests.get('http://www.kingstone.com.tw/about/about_2.asp'\
                 ).text.encode('utf-8')
soup = BeautifulSoup(r)

##alink = soup.findAll('a')
##for row in alink:
##    if row.contents:
##        branch = row.contents[0].encode('utf-8')
##        m = re.match(r'(.*?[^書]店)$', branch)
##        #print branch
##        if m is not None:
##            print m.group(1)
##只透過'a'標籤找書店名

m = soup.findAll('tr')
for row in m:
    if len(row.contents) == 13:
        print row.contents[7].text, ":",
        print row.contents[9].text
