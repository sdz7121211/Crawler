'''
Created on 2012-11-5

@author: sdz
'''
import urllib2
from BeautifulSoup import BeautifulSoup

page = urllib2.urlopen("http://www.baidu.com")
soup = BeautifulSoup(page)
for incident in soup('td', width="90%"):
    where, linebreak, what = incident.contents[:3]
    print where.strip()
    print what.strip()
    print
