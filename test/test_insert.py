from db import db_func


db = db_func.DB_Func()
db.Connect()
db.cousor.execute('insert into log_data values(null, 1, 1, 1, DB-ExecuteSql, current_date)')
db.cousor.execute('insert into log_data values(null, 5, <class @_mysql_exceptions.OperationalError@>, , DB-ExecuteSql, current_date)')
db.Close()