from analysis import analysisClassify_jd
from kernel import getHtml
from utility.queueUtility import queueFactory

queueFactory.CreatInstance(0, 1000)
html = getHtml.getHtml().getTarget('http://www.360buy.com/allSort.aspx')
print html

#queueFactory.CreatInstance(1, 1000)
#queueFactory.CreatInstance(2, 1000)

testObj = analysisClassify_jd.analysisClassify_jd(html).getResult()
print queueFactory.GetInstance(0).qsize()
while(not queueFactory.GetInstance(0).empty()):
    data = queueFactory.GetInstance(0).get()
    print data.classifyUrl