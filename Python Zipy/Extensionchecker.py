import MySQLdb
import datetime
import time
import specifictest


conn=MySQLdb.connect('localhost','root' ,'','test')
co=conn.cursor()

##TO BE LINKED PROPERLY
sql="SELECT * FROM confirmed WHERE book_id=%d"%(100001)      #connecting to confirmed.sql
co.execute(sql)
p3=co.fetchall()
sql="SELECT * FROM extension"     #connecting to confirmed.sql
co.execute(sql)
p4=co.fetchall()
s=p4[0]##s is extension time



def insertbook(book_id,model,date,pick_time,duration,timestamp,mobile):   
    sql='''INSERT INTO book (book_id , model , date , pick_time , duration , timestamp , mobile ) VALUES (%d , '%s', '%s' , '%s' , '%s' , '%s' , %d )'''%(book_id,model,date,pick_time,duration,timestamp,mobile)
    co.execute(sql)
r=[]
##FOR DUAL DAY RIDES
for q in p3:
    x=[]
    x.append(q[2])
    if len(x)>1:
        y=max(x)
    else:
        y = x[0]        ## y is confirmed date to extend

for q in p3:
    if q[2]==y:
        r=q             ##r is confirmed booking to extend

## For extension before ride begins
if r!=[]:
    if r[8]==0 or r[8]==1:
        if 'day' not in str(r[4]+s[4]):
            co.execute("TRUNCATE book")
            insertbook(s[0],str(s[1]),str(s[2]),str(r[4]),str(s[4]),str(s[5]),s[6])
            conn.commit()
            co.close()
            conn.close()
            vehicle1=specifictest.checker()
            if vehicle1==1:
                print 'not available'            ##TO BE CHANGED
            else:
                print 'yes'
        else:
            conn=MySQLdb.connect('localhost','root' ,'','test')
            co=conn.cursor()
            co.execute("TRUNCATE book")
            insertbook(s[0],str(s[1]),str(s[2]),str(r[4]),str(datetime.timedelta(days=1) - r[4] - datetime.timedelta(minutes=1)),str(s[5]),s[6])
            conn.commit()
            co.close()
            conn.close()
            vehicle1=specifictest.checker()
            if vehicle1==1:
                print 'not available'            ##TO BE CHANGED
            else:
                print 'yes'
            conn=MySQLdb.connect('localhost','root' ,'','test')
            co=conn.cursor()
            
            co.execute("TRUNCATE book")
            insertbook(s[0],str(s[1]),str(s[2]+datetime.timedelta(days=1)),datetime.timedelta(hours=0),str(r[4]+s[4] - datetime.timedelta(days=1)),str(s[5]),s[6])
            conn.commit()
            co.close()
            conn.close()
            vehicle1=specifictest.checker()
            if vehicle1==1:
                print 'not available'            ##TO BE CHANGED
            else:
                print 'yes'
            
            

##FOR REAL TIME EXTENSION (FORCE EXTENSION)
    elif r[8]==2:
        conn=MySQLdb.connect('localhost','root' ,'','test')
        co=conn.cursor()
        
        print str(r[4]+s[4])
        ##MULTI DAY EXTENSIONS
        if 'day' in str(r[4]+s[4]):
            print 'yes3'
            sql="UPDATE confirmed SET drop_time='%s' WHERE book_id=%d"%('00:00:00', r[5])
            co.execute(sql)
            sql="INSERT INTO confirmed (vehicle_id , model , date , pick_time , drop_time , book_id , mobile , timestamp , state) VALUES (%d , '%s' , '%s' , '%s' , '%s' , %d , %d , '%s' , %d)"%(r[0],str(r[1]),str(r[2]+datetime.timedelta(days=1)),'00:00:00',str(s[4]-(datetime.timedelta(days=1)-r[4])),r[5],r[6],str(r[7]),r[8])
            co.execute(sql)
            sql="SELECT * FROM confirmed where vehicle_id=%d AND date='%s' ORDER BY pick_time ASC"%(r[0],datetime.timedelta(days=1)+r[2])
            co.execute(sql) 
            t=co.fetchall()
        else:
            sql="UPDATE confirmed SET drop_time='%s' WHERE book_id=%d"%(str(r[4]+s[4]), r[5])
            co.execute(sql)
            placeholder=r[4]+s[4]
            sql="SELECT * FROM confirmed where vehicle_id=%d AND date='%s' ORDER BY pick_time ASC"%(r[0],r[2])
            co.execute(sql) 
            t=co.fetchall()
            
        
        for x in t:    
            if x[3]>r[3]:
                if x[5]!=r[5]:
                    if placeholder>x[3]:
                        if 'day' in str(placeholder-x[3]+x[4]):
                            sql="UPDATE confirmed set drop_time='%s' WHERE book_id=%d"%('23:59:00' , x[5])
                            co.execute(sql)
                            sql="INSERT INTO confirmed (vehicle_id , model , date , pick_time , drop_time , book_id , mobile , timestamp , state) VALUES (%d , '%s' , '%s' , '%s' , '%s' , %d , %d , '%s' , %d)"%(x[0],str(x[1]),str(x[2]+datetime.timedelta(days=1)),'00:00:00',str((x[4]-x[3])-(datetime.timedelta(days=1)-placeholder)),x[5],x[6],str(x[7]),x[8])
                            co.execute(sql)
                            sql="SELECT * FROM confirmed where vehicle_id=%d AND date='%s' ORDER BY pick_time ASC"%(r[0],r[2]+datetime.timedetla(days=1))
                            co.execute(sql)
                            z=co.fetchall()
                            x.append(z)
                        else:    
                            sql="UPDATE confirmed set drop_time='%s' WHERE book_id=%d"%(str((placeholder-x[3])+x[4]) , x[5])
                            co.execute(sql)
                            sql="UPDATE confirmed set pick_time='%s',state=%d WHERE book_id=%d"%(str(placeholder) , x[5] , 2)
                            co.execute(sql)
                            sql="SELECT * FROM confirmed where book_id=%d"%(x[5])
                            co.execute(sql)
                            y=co.fetchall()
                            y=y[0]
                            placeholder=y[4]
                            print placeholder
                        
                        
        conn.commit()
        co.close()
        conn.close()
                        
                




         

