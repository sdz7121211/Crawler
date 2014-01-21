import log_data,log_record,log_type
from analysis.__init__ import GoodsData

def getinstance(logType, exception ,extraMessage = '',goodsData = ""):
    
    logData = log_data.LogData()
    logData.logType = logType
    logData.exceptionType = str(type(exception)).replace("'", "@")
    if str(exception.message):
        logData.exceptionMessage = str(exception.message).replace("'", "@")
    elif str(exception):
        logData.exceptionMessage = str(exception)
    else:
        logData.exceptionMessage = '' 
    logData.extraMessage = extraMessage
    if not goodsData:
        logData.goodsData = GoodsData(goodsData)
    else:
        logData.goodsData = goodsData 
    logRecord = log_record.log_record(logData)
    logRecord.start()