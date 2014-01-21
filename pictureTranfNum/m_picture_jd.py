import m_picture_interface
from kernel import getPicture
from p_picture_jd_control import m_scan

class Picture_jd(m_picture_interface.IPicture):
    def __init__(self):
        m_picture_interface.IPicture.__init__(self)
        self.reDownloadTimes = 0
        
    def DealPicture(self,url):
        downloadPicture = getPicture.getPicture()
        data = downloadPicture.getTarget(url)
        priceStr = ''
        try:
            priceStr = m_scan.ScanPicture(data)
            priceStr = priceStr[1:]
            price = float(priceStr)
            return price
        except Exception,e:
            self.reDownloadTimes += 1
            if self.reDownloadTimes > 3:
                raise e
            else:
                return self.DealPicture(url)
        