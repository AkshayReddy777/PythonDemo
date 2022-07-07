import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='akshay', passwd='1234', database = 'telusuko')

mycursor = mydb.cursor()
result = mycursor.fetchall()
mycursor.execute('select * from student')
#for i in mycursor:
 #   print(i)
for i in result:
    print(i)