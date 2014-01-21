import m_scanNode
import m_init

def ScraPicture(picture, pic):
    pictureList = []
    key = False
    test = True
    (width,heigth) = pic.size
    for i in range(width):
        for j in range(heigth):
            pixel = picture[i, j]
                
            if key == False:
                if not m_init.CheckIsBlank(pixel):
                    key = True
                    test = True
                    scan = m_scanNode.ScanNode()
                    scan.startWidth = i
                    pictureList.append(scan)
            else:
                if i == pictureList[len(pictureList) - 1].startWidth:
                    continue
                else:
                    if not m_init.CheckIsBlank(pixel):
                        test = False
        if key == True:
            if test == False:
                test = True
            else:
                if i != pictureList[len(pictureList) - 1].startWidth:
                    pictureList[len(pictureList) - 1].endWidth = i - 1
                    test = False
                    key = False
    if key == True:
        pictureList[len(pictureList) - 1].endWidth = width - 1

    key = False
    test = False
    for scan in pictureList:
        for i in range(heigth):
            for j in range(scan.startWidth, scan.endWidth+1):
                pixel = picture[j, i]
                if key == False:
                    if not m_init.CheckIsBlank(pixel):
                        test = True
                        key = True
                        scan.startHeigth = i
                else:
                    if i == scan.startHeigth:
                        continue
                    else:
                        if not m_init.CheckIsBlank(pixel):
                            test = False
            if key == True:
                if test == False:
                    test = True
                else:
                    if i != scan.startHeigth:
                        scan.endHeigth = i - 1
                        test = False
                        key = False
        if key == True:
            pictureList[len(pictureList) - 1].endHeigth = heigth - 1
    return pictureList
