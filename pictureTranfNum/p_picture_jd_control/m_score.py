class Score():
    def __init__(self,s,dt):
        self.score = s
        self.dt = dt

FError = 5
SError = 3
TError = 1
        
def GetScore(dt, targetDt):
    all = abs(dt.TB[0][0] - targetDt.TB[0][0])
    fScore = 100 - (int)(all/1) * FError
    
    for i in range(4):
        all += abs(dt.TB[1][i] - targetDt.TB[1][i])
    sScore = 100 - (int)(all / 4) * SError
    
    for i in range(16):
        all += abs(dt.TB[2][i] - targetDt.TB[2][i])
    tScore = 100 - (int)(all / 16) * TError
    
    return fScore + sScore + tScore
