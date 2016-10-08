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
    if z<datetime.datetime.now().time() and a<datetime.datetime.now().time():
        continue
    else:
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

for y in array:
    if y[0]=='FZ-FI v2':
        fz.append(str(y[1]))
        fz.append(str(y[2]))
    if y[0]=='Pulsar 150':
        pulsar.append(str(y[1]))
        pulsar.append(str(y[2]))
    if y[0]=='Fascino':
        fascino.append(str(y[1]))
        fascino.append(str(y[2]))

data = {'FZ-FI v2': fz , 'Pulsar 150': pulsar , 'Fascino':fascino}
        

with open('availability.txt', 'w') as outfile:
    json.dump(data, outfile)



conn.commit()
co.close()
conn.close()
