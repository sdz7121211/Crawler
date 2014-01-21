three_tuple = 1242801948
four_tuple = 1648862477

def CheckIsBlank(pixelTupleFormat):
    pixelTupleStr = str(pixelTupleFormat).replace('(', '').replace(')','')
    pixelItemList = pixelTupleStr.split(",")
    pixelList = []
    for pixel in pixelItemList:
        pixelList.append(int(pixel))
    pixelTuple = tuple(pixelList)

    hashValue = pixelTuple.__hash__()
    if len(pixelTuple) == 3:
        if hashValue == three_tuple:
            return True
        else:
            return False
    else:
        if hashValue == four_tuple:
            return True
        else:
            return False