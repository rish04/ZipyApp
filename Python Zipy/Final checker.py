import MySQLdb
import datetime
import time
import zipytest


conn=MySQLdb.connect('localhost','root' ,'','test')
co=conn.cursor()


############# TO BE REMOVED#############
co.execute("SELECT * FROM book")
dual = co.fetchall()
dual=dual[0]

        

conn.commit()
co.close()
conn.close()

if 'day' in str(dual[3]+dual[4]):
    conn=MySQLdb.connect('localhost','root' ,'','test')
    co=conn.cursor()
    number=int(str(dual[3]+dual[4])[0])
    sql="UPDATE book SET duration='%s'"%(str(datetime.timedelta(days=1) - dual[3] - datetime.timedelta(minutes=1)))
    co.execute(sql)
    conn.commit()
    co.close()
    conn.close()
    vehicle1=zipytest.checker()
    if vehicle1==1:
        print 'Just got booked'##TO BE CHANGED
    else:
        print 'yes'
        
        for n in range(number):
            print n
            if n!=(number-1):
                conn=MySQLdb.connect('localhost','root' ,'','test')
                co=conn.cursor()
                
                sql="UPDATE book SET date='%s',pick_time='%s',duration='%s' WHERE book_id=%d"%(str(dual[2]+datetime.timedelta(days=1+n)),'00:00:00','23:59:00' ,dual[0])
                co.execute(sql)
                conn.commit()
                co.close()
                conn.close()
                vehicle1=zipytest.checker()
                if vehicle1==1:
                    print 'Just got booked'
                
                else:
                    print 'yes'
            if n==(number-1):
                conn=MySQLdb.connect('localhost','root' ,'','test')
                co=conn.cursor()
                co.execute("SELECT * FROM book")
                test=co.fetchall()
    
                sql="UPDATE book SET date='%s',pick_time='%s',duration='%s' WHERE book_id=%d"%(str(dual[2]+datetime.timedelta(days=1+n)),'00:00:00' , str(dual[4]+dual[3]-datetime.timedelta(days=number)) , dual[0])
                co.execute(sql)
                co.execute("SELECT * FROM book")
                test=co.fetchall()
                conn.commit()
                co.close()
                conn.close()
                vehicle1=zipytest.checker()
                if vehicle1==1:
                    print 'Just got booked'
                
                else:
                    print 'yes'
            
else:
    vehicle1=zipytest.checker()
    if vehicle1==1:
        print 'Just got booked'            ##TO BE CHANGED
    else:
        print 'yes'
##FINISHED
##
##
##
##
##
##
##
