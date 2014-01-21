#coding=gbk
import MySQLdb
class DB_Func(object):
    def __init__(self,):
        self.host = 'localhost'
        self.username = 'root'
        self.password = 'root'
        self.dbName = 'online_shopping'
        self.charset = 'gbk'
        self.con = None
        self.cousor = None
        
    def Connect(self):
        self.con = MySQLdb.connect(host = self.host,
                                       user = self.username,
                                       passwd = self.password,
                                       db = self.dbName,
                                       charset = self.charset)
        self.cousor = self.con.cursor()
    
    def Close(self):
        self.cousor.close()
        self.con.close()
        self.con = None
        self.cousor = None
        
    def IsClose(self):
        if self.con == None:
            return True
        else:
            return False
        
        
#test = []
#test.append(DB_Func())
#test.append(DB_Func())
#test.append(DB_Func())
#for ins in test:
#    ins.Connect()
    