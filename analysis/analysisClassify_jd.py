#!/usr/bin/python
# -*- coding: utf-8 -*-  
import sys
from BeautifulSoup import BeautifulSoup
from utility.queueUtility import queueFactory
from __init__ import GoodsData

class analysisClassify_jd():
    '''
                                   获取     网站名     分类     分类URL                                         
    '''

    def __init__(self,html):
        self.html = html
        self.header = 'http://www.360buy.com/'
    
    def getResult(self):       
        try:
            soup = BeautifulSoup(self.html)
            soupDiv = soup.findAll('div', {'class':'m'})
            print '过滤掉了书籍 ','  m_crawlClassify_jd'       
            for j in range(1,len(soupDiv)-1,1):
                soup = BeautifulSoup(str(soupDiv[j]))
                element = soup('em')
                for i in range(len(element)):
                    '''实例化一个classifyData数据结构对象'''
                    try:
                        '''各个字段赋值'''
                        data = GoodsData()
                        data.websiteName = 'jd'
                        data.classifyName = str(element[i].a.string)
                        classifyUrl = str(element[i].a['href'])
                        if classifyUrl.startswith('/'):
                            data.classifyUrl = ''.join([self.header[:-1],classifyUrl])
                        else:
                            data.classifyUrl = ''.join([self.header,classifyUrl])
                        queueFactory.GetInstance(0).put(data)
                    except:
                        print 'analysisClassify_jd',sys.exc_info()
        except:
            print 'analysisClassify_jd',sys.exc_info()
            
           
            
        
                    
        