import string
import m_dTable
import sys

DataFileName = "c:\\data.dat";
dtList = []

def Load():
    op = open(DataFileName,'r')
    tmp = []
    content = op.read()
    op.close()
    data = content.split(' ')
    for d in data:
        try:
            tmp.append(string.atoi(d))
        except:
            print sys.exc_info()[0]

    dt = m_dTable.LoadData(tmp)
    
    for d in dt:
        dtList.append(d)