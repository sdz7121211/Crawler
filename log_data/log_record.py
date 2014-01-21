from db import db_func
import threading
import log_data
from analysis import GoodsData

class log_record(threading.Thread):

    def __init__(self,logdata):
        threading.Thread.__init__(self) 
        self.logdata = log_data.LogData(logdata)
        self.data = GoodsData(self.logdata.goodsData)
    
    def run(self):
#        try:
#            print type(self.logdata.exceptionMessage),'2222222',len(self.logdata.exceptionMessage)
            print self.logdata.logType, self.logdata.exceptionType, self.logdata.exceptionMessage, self.logdata.extraMessage
            db = db_func.DB_Func()
            db.Connect()
            self.logdata.exceptionMessage = str(self.logdata.exceptionMessage).replace("'", "@")
            self.logdata.exceptionMessage = str(self.logdata.exceptionMessage).replace(''''"''', "#")            
            sql1 = "insert into log_data(LogType, ExceptionType, ExceptionMessage, AppendMessage, LogTime) values({0}, '{1}', '{2}', '{3}', current_date)"\
                    .format(self.logdata.logType, self.logdata.exceptionType, self.logdata.exceptionMessage, self.logdata.extraMessage)
            print sql1
            db.cousor.execute(sql1)
            db.con.commit()
            if self.data.goodsName:
                sql2 = "insert into log_detail(LogId, GoodsId, GoodsName, GoodPriceUrl, GoodsPrice,  GoodsImageUrl, GoodsUrl, ClassifyName, WebsiteName, EvaluateNum, EvaluateUrl, ClassifyUrl) values({0}, '{1}', '{2}', '{3}', {4}, '{5}', '{6}', '{7}',  '{9}', {8}, '{10}', '{11}')".\
                        format(self.logdata.logType, self.data.goodsId, self.data.goodsName, self.data.goodsPriceUrl, self.data.goodsPrice, self.data.goodsImageUrl, self.data.goodsUrl, self.data.classifyName, self.data.websiteName, self.data.evaluateNum, self.data.evaluateUrl, self.data.classifyUrl)
                print "log_record sql2:", sql2
                db.cousor.execute(sql2)
                db.con.commit()
            db.Close()
#        except:
#            print 'log_record   ',sys.exc_info()