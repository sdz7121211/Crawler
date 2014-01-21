#!/usr/bin/python
# -*- coding: utf-8 -*-  
class GoodsData():
    def __init__(self, data = None):
        self.data = data
        self.goodsId = ''       #网站内部商品编码
        self.goodsName = ''    #商品名称
        self.goodsPriceUrl = ''   #商品价格
        self.goodsPrice = ''    #商品价格
        self.goodsImageUrl = ''#商品图片URL
        self.goodsUrl = ''     #商品详细信息页URL
        self.classifyName = '' #商品分类
        self.websiteName = ''  #网站名字
        self.evaluateNum = ''  #评价数量
        self.evaluateUrl = ''  #评论起始页URL
        self.classifyUrl = ''  #商品所在分页URL
        self.sourceCode = ''
        self.pageNum = ''
        '''类型转换'''
        if data:
            self.goodsId = data.goodsId
            self.goodsName = data.goodsName
            self.goodsPriceUrl = data.goodsPriceUrl
            self.goodsPrice = data.goodsPrice
            self.goodsImageUrl = data.goodsImageUrl
            self.goodsUrl = data.goodsUrl
            self.classifyName = data.classifyName
            self.websiteName = data.websiteName
            self.evaluateNum = data.evaluateNum
            self.evaluateUrl = data.evaluateUrl
            self.classifyUrl = data.classifyUrl
            try: 
                self.sourceCode = data.sourceCode
            except:
                self.sourceCode = ''
            self.pageNum = data.pageNum          
    def __str__(self):
        if self.data:
            return self.goodsId,self.goodsName,self.goodsPrice,self.goodsImageUrl,self.goodsUrl,self.classifyName,self.websiteName,self.evaluateNum,self.evaluateUrl,self.classifyUrl,'html 源代码 此处省略'
        else:
            return None
                
                
                
