#!/usr/bin/python
# -*- coding: utf-8 -*-  
import StringIO
import gzip
import re
from urlparse import urlparse
import httplib
from log_data import log_recordFactory,log_type

class getHtml():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.headers = {'Accept':'textml,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-encoding':'gzip, deflate',
           'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
           'Connection':'keep-alive',
           "User-agent":"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20100101 Firefox/12.0"}

        
        
    def getTarget(self, url, method="GET", body=None, timeout=5, currentRequestTimes=0):    
        code = None
        try:     
            parsed = urlparse(url)       
            webUrl = parsed.netloc
            path = parsed.path       
            conn = httplib.HTTPConnection(webUrl, timeout = 10)           
            conn.request("GET", path, headers = self.headers)      
            response = conn.getresponse()
            
            while response.status == 302:
                url =  response.msg.get('Location')
                print '302',  ' getHtml ',url
                conn.close()
                
                parsed = urlparse(url)       
                webUrl = parsed.netloc
                path = parsed.path       
                conn = httplib.HTTPConnection(webUrl, timeout = 10)           
                conn.request("GET", path, headers = self.headers)      
                response = conn.getresponse()
               
            code = response.read()
            
            charset = response.msg.get('Content-Type')
            if charset.find('charset') != -1:
                charset = charset.split('charset=')[1].lower()
            else:
                charset = None
                
            encoding = response.msg.get('Content-Encoding')
                   
            if encoding == 'gzip':
                buf = StringIO.StringIO(code)
                f = gzip.GzipFile(fileobj=buf)
                code = f.read()    
            if charset == None:
                m_charset = re.search('content.*charset\s?=\s?([\w\d-]+?)"', code, re.IGNORECASE)
                charset = m_charset.group(1)           
            code = code.decode(charset,'ignore')            
            return code
        except Exception,e:
            log_recordFactory.getinstance(log_type.getHtml, e, extraMessage = url) 
            