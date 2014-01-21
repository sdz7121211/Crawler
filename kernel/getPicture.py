#!/usr/bin/python
# -*- coding: utf-8 -*-  
import socket
from urlparse import urlparse
import httplib
import StringIO
import gzip
from log_data import log_recordFactory,log_type

class getPicture():
    '''
    classdocs
    '''


    def __init__(self):
        self.code = None
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
                        
            if response.status == 302:
                url =  response.msg.get('Location')
                conn.close()                
                parsed = urlparse(url)       
                webUrl = parsed.netloc
                path = parsed.path
                conn = httplib.HTTPConnection(webUrl, timeout = 10)           
                conn.request("GET", path, headers = self.headers)      
                response = conn.getresponse()
                
            self.code = response.read()            
            encoding = response.msg.get('Content-Encoding')
                   
            if encoding == 'gzip':
                buf = StringIO.StringIO(self.code)
                f = gzip.GzipFile(fileobj=buf)
                self.code = f.read()   
            conn.close()
            return self.code
        except Exception as e:
            # the html of URL is not exists
            if type(e) == socket.gaierror:
                log_recordFactory.getinstance(log_type.getPicture, e, extraMessage = url) 
            # socket connect error,maybe two reason:
            # 1.the host computer refuse to connect
            # 2.the host of the url is not exist
            elif type(e) == socket.error:
                log_recordFactory.getinstance(log_type.getPicture, e, extraMessage = url) 
            # HTTPConnect is timeout
            elif type(e) == socket.timeout:
                currentRequestTimes += 1
                if currentRequestTimes>self.maxRequestTimes:
                    log_recordFactory.getinstance(log_type.getPicture, e, extraMessage = url) 
                else:
                    return self.getTarget(url, method, body, timeout,currentRequestTimes)
            # read error，maybe two reason:
            #1.read is interrupted
            #2.read zero bytes
            elif type(e) == httplib.IncompleteRead:
                currentRequestTimes += 1
                if currentRequestTimes>self.maxRequestTimes:
                    log_recordFactory.getinstance(log_type.getPicture, e, extraMessage = url) 
                else:
                    return self.getPicture(url, method, body, timeout,currentRequestTimes)
            else:
                log_recordFactory.getinstance(log_type.getPicture, e, extraMessage = url)          
            log_recordFactory.getinstance(log_type.getPicture, e, extraMessage = url)         