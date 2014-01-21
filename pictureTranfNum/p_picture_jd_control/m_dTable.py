class DTable(object):
    def __init__(self, Code, fData, sData, tData):
        self.TB = []
        self.Code = Code
        self.TB.append(fData)
        self.TB.append(sData)
        self.TB.append(tData)
    
def LoadData(valueList):
    dtList = []
    fData = []
    sData = []
    tData = []
    code = 0

    index = 0
    i = 0
    while True:
        if i < len(valueList):
            for j in range(22):
                if j == 0:
                    code = valueList[i]
                if j == 1:
                    fData.append(valueList[i])
                if j>1:
                    if j <= 5:
                        index += 1
                        sData.append(valueList[i])
                if j>5:
                    if j == 6:
                        index = 0
                    index += 1
                    tData.append(valueList[i])
                    if j == 21:
                        index = 0
                        dt = DTable(code, fData, sData, tData)
                        dtList.append(dt)
                        fData = []
                        sData = []
                        tData = []
                i += 1
        else:
            break
    return dtList