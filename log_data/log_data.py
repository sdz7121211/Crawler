#!/usr/bin/python
# -*- coding: utf-8 -*- 
from analysis import GoodsData

 
class LogData():
    def __init__(self, data = None):
        self.logType = ''       #错误类型
        self.exceptionType = '' #异常类型
        self.exceptionMessage = ''   #异常字符串
        self.goodsData = GoodsData() #异常数据
        self.extraMessage = '' #附加信息
        '''类型转换'''
        if data:
            self.logType = data.logType
            self.exceptionType = data.exceptionType
            self.exceptionMessage = data.exceptionMessage
            self.goodsData = GoodsData(data.goodsData)
            self.extraMessage = data.extraMessage