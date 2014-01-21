#!/usr/bin/python
# -*- coding: utf-8 -*-  
import Queue

instanceList = {}


def GetInstance(queue_id):
    return instanceList[queue_id]


def CreatInstance(queue_id, maxNum = 0):
    obj = Queue.Queue(maxsize = maxNum)
    instanceList[queue_id] = obj

##!/usr/bin/python
## -*- coding: utf-8 -*-  
##from queuesControler import queuesControler
#import dataQueue
#
#
##QueuesControlerInstance = None
#QueuesInstance = []
##
##
##def getQueuesControler():
##    global QueuesControlerInstance
##    if not QueuesControlerInstance:
##        QueuesControlerInstance = queuesControler()
##        print "鏂板缓  getQueuesControler"
##        return QueuesControlerInstance
##    else:
##        print "杩斿洖宸插瓨鍦ㄧ殑  getQueuesControler"
##        return QueuesControlerInstance
#    
#def getDataQueueInstance(maxNum = 0,description = None):
#    dataQueueInstance = dataQueue.dataQueue(maxNum,description)
#    return dataQueueInstance
#
#    
#if  QueuesInstance == []: 
#    print '鍒濆鍖�涓槦鍒�  
#    QueuesInstance.append(getDataQueueInstance(1000,"鑾峰彇 '缃戠珯鍚� '鍒嗙被URL' '鍒嗙被鍚�"))
#    QueuesInstance.append(getDataQueueInstance(1000,"锛�缃戠珯鍚� '鍒嗙被URL' '鍒嗙被鍚�锛夎幏鍙� '鍒嗙被URL'鎵�寚鍚戠殑婧愪唬鐮�))
#    QueuesInstance.append(getDataQueueInstance(20000,"锛�缃戠珯鍚� '鍒嗙被URL' '鍒嗙被鍚�锛�'鍒嗙被URL'鎵�寚鍚戠殑婧愪唬鐮� 鑾峰彇鍏朵粬鐨�))