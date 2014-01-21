from analysis import __init__

def InsertSql(goodsData):
    goodsData = __init__.GoodsData(goodsData)
    sql = ''.join(['INSERT INTO t_init_data VALUES(',
                   'null,',
                   "'",goodsData.goodsId,"',",
                   '''"''',goodsData.goodsName,'''",''',
                   "'",goodsData.goodsPriceUrl,"',",
                   str(goodsData.goodsPrice),",",
                   "'",goodsData.goodsImageUrl,"',",
                   "'",goodsData.goodsUrl,"',",
                   "'",goodsData.classifyName,"',",
                   "'",goodsData.websiteName,"',",
                   str(goodsData.evaluateNum),",",
                   "'",goodsData.evaluateUrl,"',",
                   "'",goodsData.classifyUrl,"',",
                   'current_date',",",
                   str(goodsData.pageNum),")"
                   ])
    return sql
##from analysis import __init__
#
#def InsertSql(goodsData):
##    goodsData = __init__.GoodsData(goodsData)    
#        sql = ''.join(['INSERT INTO t_init_data VALUES(',
#                       'null,',
#                       "'",goodsData.goodsId,"',",
#                       str(goodsData.classifyName).replace("'", "\'"),",",
#                       str(goodsData.goodsPrice),",",
#                       "'",goodsData.goodsImageUrl,"',",
#                       "'",goodsData.goodsUrl,"',",
#                       "'",goodsData.classifyName,"',",
#                       "'",goodsData.websiteName,"',",
#                       str(goodsData.evaluateNum),",",
#                       "'",goodsData.evaluateUrl,"',",
#                       "'",goodsData.classifyUrl,"',",
#                       'current_date',",",
#                       str(goodsData.pageNum),")"
#                       ])
#        return sql