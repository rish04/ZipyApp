import MySQLdb
import datetime
import time
import zipytestswa


conn=MySQLdb.connect('localhost','root' ,'','test')
co=conn.cursor()

print datetime.date.today()
sql='SELECT * FROM confirmed WHERE date >= "%s"'%(datetime.date.today())
co.execute(sql)
x=co.fetchall()

def insertswa(book_id,model,date,pick_time,duration,timestamp,mobile):
    co.execute("TRUNCATE book")
    sql='''INSERT INTO swa (book_id , model , date , pick_time , duration , timestamp , mobile ) VALUES (%d , '%s', '%s' , '%s' , '%s' , '%s' , %d )'''%(book_id,model,date,pick_time,duration,timestamp,mobile)
    co.execute(sql)
dt = datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()) + datetime.timedelta(minutes=30)
print dt.time()   
for y in range(24):
    insertswa(000000 , 'Pulsar 150', '%s' , '%s' , '%s' , '%s' , 0000000000)%(datetime.date.today(),now,now+datetime.timedelta(hours=1),datetime.datetime.now().time())



conn.commit()
co.close()
conn.close()
