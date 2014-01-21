#!/usr/bin/python
# -*- coding: utf-8 -*-  
import db_func
import threading
import db_insert_init_data
import time
from utility.queueUtility import queueFactory
from log_data import log_recordFactory,log_type

class DB():
    def __init__(self):
        self.db = db_func.DB_Func()
        self.logrecord = None 
        self.testThread = threading.Thread(target = self.WriteToDB)
        self.testThread.start()       
    
    def WriteToDB(self):
        while True:
            if queueFactory.GetInstance(2).empty() != True:
                goodsData = queueFactory.GetInstance(2).get()
                if self.db.IsClose() == True:
                    self.db.Connect()
                self.ExecuteSql(goodsData)
            else:
                if self.db.IsClose() == False:
                    self.db.Close()
                    time.sleep(5)
                                
    def ExecuteSql(self,data):  
        sql = ''
        try:
            sql = db_insert_init_data.InsertSql(data)
            self.db.cousor.execute(sql)
            self.db.con.commit()
        except Exception as e:
            log_recordFactory.getinstance(log_type.db_insert, e, extraMessage = 'DB-ExecuteSql')