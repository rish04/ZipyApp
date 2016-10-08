import MySQLdb
import datetime
import time
import json


conn=MySQLdb.connect('localhost','root' ,'','test')
co=conn.cursor()

sql = "SELECT * FROM confirmed WHERE date = '%s'"%(datetime.date.today())
co.execute(sql)
x=co.fetchall()
array=[]

for y in x:
    z=y[3]+datetime.datetime.min
    a=y[4]+datetime.datetime.min
    z=z.time()
    a=a.time()
    if z>=datetime.datetime.now().time() and a<=datetime.datetime.now().time():
        array.append(y)
fz=[]
pulsar=[]
fascino=[]
for y in array:
    z=y[3]+datetime.datetime.min
    a=y[4]+datetime.datetime.min
    z=z.time()
    a=a.time()
    array[array.index(y)]=[y[1],z,a]

available = '000'
if array==[]:
    available='111'
else:
    for y in array:
        if y[0]=='Fascino':
            available[0]='1'
        if y[0]=='Pulsar 150':
            available[1]='1'
        if y[0]=='FZ-FI v2':
            available[2]='1'
        
with open('availability.txt', 'w') as outfile:
    json.dump(available, outfile)



conn.commit()
co.close()
conn.close()
