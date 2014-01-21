import db

db_ary = []

def GetInstance():
    if db_ary == []:
        d = db.DB()
        db_ary.append(d)
    return db_ary[0]