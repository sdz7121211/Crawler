import m_scanPicture
import m_scanPixelValue

def GetPictureValue(picture, pic):
    sList = m_scanPicture.ScraPicture(picture, pic)
    
    valueList = []
    count = 0
    
    for scan in sList:
        valueList.append(-1)
        
        value = 0
        value = m_scanPixelValue.GetValue(scan.startWidth, scan.endWidth, scan.startHeigth, scan.endHeigth, picture)
        valueList.append(value)
        
        
        span = 2
        spanWidth = (int)((scan.endWidth - scan.startWidth + 1) / span)
        spanHeigth = (int)((scan.endHeigth - scan.startHeigth + 1) / span)

        for i in range(span):
            for j in range(span):
                if spanWidth == 0:
                    if i >= (scan.endWidth - scan.startWidth + 1):
                        valueList.append(0)
                        continue

                if spanHeigth == 0:
                    if j >= (scan.endHeigth - scan.startHeigth + 1):
                        valueList.append(0)
                        continue

                if i == span - 1 & j == span - 1:
                    value = m_scanPixelValue.GetValue(scan.startWidth + spanWidth * i, scan.endWidth, scan.startHeigth + spanHeigth * j, scan.endHeigth, picture)
                    valueList.append(value)
                else:
                    value = m_scanPixelValue.GetValue(scan.startWidth + spanWidth * i, scan.startWidth + spanWidth * (i + 1) - 1, scan.startHeigth + spanHeigth * j, scan.startHeigth + spanHeigth * (j + 1) - 1, picture)
                    valueList.append(value)

        
        span = 4
        spanWidth = (int)((scan.endWidth - scan.startWidth + 1) / span)
        spanHeigth = (int)((scan.endHeigth - scan.startHeigth + 1) / span)
        
        for i in range(span):
            for j in range(span):
                if spanWidth == 0 & i >= (scan.endWidth - scan.startWidth + 1):
                    valueList.append(0)
                    continue

                if spanHeigth == 0 & j >= (scan.endHeigth - scan.startHeigth + 1):
                    valueList.append(0)
                    continue

                if i == span - 1 & j == span - 1:
                    value = m_scanPixelValue.GetValue(scan.startWidth + spanWidth * i, scan.endWidth, scan.startHeigth + spanHeigth * j, scan.endHeigth, picture)
                    valueList.append(value)
                else:
                    value = m_scanPixelValue.GetValue(scan.startWidth + spanWidth * i, scan.startWidth + spanWidth * (i + 1) - 1, scan.startHeigth + spanHeigth * j, scan.startHeigth + spanHeigth * (j + 1) - 1, picture)
                    valueList.append(value)
                    
    return valueList
