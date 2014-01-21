#!/usr/bin/python
# -*- coding: utf-8 -*-  
from BeautifulSoup import BeautifulSoup
from utility.queueUtility import queueFactory
import __init__
from pictureTranfNum import m_picture_factory
import re
import threading
import time
from log_data import log_type,log_recordFactory


class analysisItems(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.logrecord = '' 
        self.data = __init__.GoodsData()
        self.transformPicture = m_picture_factory.GetInstance()
        self.thread_stop = False
        
    def getResult(self):
            soup = ''
            try:
                soup = BeautifulSoup(self.data.sourceCode)
            except Exception as e:
                print e, soup
            soup = soup.find('ul', {'class':'list-h'})
            try:
                for i in range(len(soup('li'))):              
                    tempsoup = BeautifulSoup(str(soup('li')[i]))                 
                    soupDiv = tempsoup.find('div',{'class':'p-img'})
                    self.data.goodsUrl = soupDiv.find('a')['href']
                    self.data.goodsId = self.data.goodsUrl.split('/')[-1].split('.')[0]
                    try:
                        self.data.goodsImageUrl = soupDiv.find('img')['src']
                    except:
                        self.data.goodsImageUrl = soupDiv.find('img')['src2']                                
                    soupDiv = tempsoup.find('div', {'class':'p-name'}).a
                    soupTmp = soupDiv.find('font')
                    soupDiv = str(soupDiv).replace(str(soupTmp),'')
                    soupTmp = BeautifulSoup(soupDiv)
                    self.data.goodsName = soupTmp.a.string
                    
                    soupDiv = tempsoup.find('div', {'class':'p-price'})
                    imgURL = soupDiv.find('img')['src']
                    self.data.goodsPriceUrl = imgURL
                    try:
                        self.data.goodsPrice = self.transformPicture.DealPicture(str(imgURL)) 
                    except:
                        self.data.goodsPrice = 0 
                    soupDiv = tempsoup.find('div',{'class':'extra'})
                    evaluateNum = str(soupDiv.a.string)
                    def StringToInt(strr):
                        pattern = re.compile('\\d*') 
                        if not strr:
                            return 0
                        match = pattern.findall(strr)
                        for item in match:
                            if len(item):
                                return int(item)
                    self.data.evaluateNum = StringToInt(evaluateNum)
                    self.data.evaluateUrl = soupDiv.a['href']
                    ItemData = __init__.GoodsData(self.data)
                    del ItemData.sourceCode
                    ItemData.goodsName = str(ItemData.goodsName).replace('''"''', "%")
                    queueFactory.GetInstance(2).put(ItemData)
            except Exception as e:
                log_recordFactory.getinstance(log_type.analysis_Item, e, extraMessage = '执行类 analysisItems 的 函数getResult 出错', goodsData = self.data)
                
    def run(self):
        while not self.thread_stop:
            if queueFactory.GetInstance(1).empty() != True:
                self.data = queueFactory.GetInstance(1).get()
                self.getResult()
                time.sleep(0.1)
            else:
                time.sleep(2)
    def StopThread(self):
        self.thread_stop = True