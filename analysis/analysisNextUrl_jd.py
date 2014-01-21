#!/usr/bin/python
# -*- coding: utf-8 -*-  

from BeautifulSoup import BeautifulSoup
from utility.queueUtility import queueFactory
from kernel import getHtml
from __init__ import GoodsData
import threading
import time
from db import db_func
from log_data import log_recordFactory,log_type


class analysisNextUrl(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self) 
        self.logrecord = ''
        self.data = None
        self.headUrl = 'http://www.360buy.com/products/'
        self.objHtml = getHtml.getHtml()
        self.countPage = 0
        self.thread_stop = False
        self.sleepTime = 10
        
        
        
    def getResult(self,html):
        if html == None:
            return False
        try:
            soup = BeautifulSoup(html)
            html_a = soup.find('a',{'class':'next'})
            if html_a:
                nextUrl = str(html_a['href'])
                if nextUrl.startswith('/'):
                    return ''.join([self.headUrl[:-1],nextUrl])  
                return ''.join([self.headUrl,nextUrl])            
            else:
                return False
        except Exception as e:
            log_recordFactory.getinstance(log_type.analysis_nextUrl, e, extraMessage = self.countPage, goodsData = self.data)      
    
    
    def crawlPage(self,nextUrl = ''):
        self.countPage = 0        
        while(nextUrl):
            data = GoodsData(self.data)
            data.sourceCode = self.objHtml.getTarget(nextUrl)
            self.data.classifyUrl = nextUrl
            data.classifyUrl = nextUrl
            self.countPage+=1
            data.pageNum = self.countPage
            queueFactory.GetInstance(1).put(data)    
            nextUrl = self.getResult(data.sourceCode)  
            time.sleep(0.2)                     
        print self.data.classifyName,'already download total pages is',self.countPage
        self.storeDB()
        
    def storeDB(self):
        try:       
            db = db_func.DB_Func()
            db.Connect()
            sql = "insert into completed_classify(ClassifyName, ClassifyUrl, TotalPages) values('{0}', '{1}', {2})".\
                    format(self.data.classifyName, self.data.classifyUrl, self.countPage)
            db.cousor.execute(sql)
            db.con.commit()
            db.Close()
        except Exception as e:
            print "analysisNextUrl.storDB", self.data.classifyName
            log_recordFactory.getinstance(log_type.db_insert, e)
        
        
    def run(self):
        while not self.thread_stop:
            if queueFactory.GetInstance(0).empty() == False:
                self.data = queueFactory.GetInstance(0).get()
                self.crawlPage(self.data.classifyUrl)
                time.sleep(self.sleepTime)
            else:
                time.sleep(5)
                
    def StopThread(self):
        self.thread_stop = True
        