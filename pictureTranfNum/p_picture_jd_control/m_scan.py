import Image
import m_scanPictureValue
import m_dTable
import m_dFactory
import m_score
import os
import ImageFile

def ScanPicture(data):
    p = ImageFile.Parser()
    p.feed(data)
    pic = p.close()
    picture = pic.load()
    if m_dFactory.dtList == []:
        m_dFactory.Load()
    sb = ''
    
    value = m_scanPictureValue.GetPictureValue(picture, pic)
    
    dtList = m_dTable.LoadData(value)

    for dt in dtList:
        CheckList = []
        for ds in m_dFactory.dtList:
            score = m_score.GetScore(dt,ds)
            CheckList.append(m_score.Score(score,ds))
    
        result = m_score.Score(-1000,m_dTable.DTable(0,None,None,None))
        
        for s in CheckList:
            if s.score > result.score:
                result = s
                
        tt = chr(result.dt.Code)
        sb = ''.join((sb,tt))
    return sb
    
