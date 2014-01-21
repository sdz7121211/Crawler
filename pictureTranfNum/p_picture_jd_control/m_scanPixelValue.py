import m_init
def GetValue(startWidth, endWidth, startHeigth, endHeigth, picture):
    if startWidth - endWidth == 1:
        endWidth = startWidth
    if startHeigth - endHeigth == 1:
        endHeigth = startHeigth
    number = 0
    for i in range(startWidth, endWidth+1):
        for j in range(startHeigth, endHeigth+1):
            pixel = picture[i, j]
            if not m_init.CheckIsBlank(pixel):
                number += 1
    value = (int)(((number * 1.00) / ((endWidth - startWidth + 1) * (endHeigth - startHeigth + 1))) * 100)
    return  value