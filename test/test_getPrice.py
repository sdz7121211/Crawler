from pictureTranfNum import m_picture_factory
from kernel import getPicture
import time


#getpicture = getPicture.getPicture()
#result = getpicture.getTarget('http://price.360buyimg.com/gp313606,1.png')
#print result
while True:
    test = m_picture_factory.GetInstance()
    print test.DealPicture('http://price.360buyimg.com/gp313606,1.png')
    time.sleep(1)