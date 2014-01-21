#!/usr/bin/python
# -*- coding: utf-8 -*-  
from utility.queueUtility import queueFactory
from kernel import getHtml
from analysis import analysisClassify_jd,analysisNextUrl_jd,analysisItems_jd
import threading
from db import m_db_factory
import time

html = getHtml.getHtml().getTarget('http://www.360buy.com/allSort.aspx')
queueFactory.CreatInstance(0, 2000)
queueFactory.CreatInstance(1, 20)
queueFactory.CreatInstance(2, 100)

def start ():
    analysisClassify_jd.analysisClassify_jd(html).getResult()
    module_2 = []
    module_2.append(analysisNextUrl_jd.analysisNextUrl())
    module_2.append(analysisNextUrl_jd.analysisNextUrl())
    module_2[0].start()
    module_2[1].start()
    module_3 = []
    for i in range(40):
        module_3.append(analysisItems_jd.analysisItems())
        module_3[i].start()
    m_db_factory.GetInstance()
    print queueFactory.GetInstance(0).qsize()
    while True:
        arry1_size = queueFactory.GetInstance(1).qsize()
        arry2_size = queueFactory.GetInstance(2).qsize()
        print "队列   1   " ,arry1_size,\
              "队列  2   " ,arry2_size
#        if arry1_size!=0 and (arry2_size/arry1_size) > 10 and len(module_3)<= 50:
#            instance_analysisItems_jd = analysisItems_jd.analysisItems()
#            print "新建第",len(module_3)+1,"个  module_3 线程"
#            instance_analysisItems_jd.start() 
#            module_3.append(instance_analysisItems_jd)
        time.sleep(10)
            



#print '1'
#
#print '2'
#module_3 = analysisItems_jd.analysisItems().start()
#print '3'
#weiteTodb = m_db_factory.GetInstance()

threading.Thread(target = start).start()

'''
    队列  1 存放的是包含源代码的队列 
   队列  2 分析完成 等待最终存入数据库的队列
'''
