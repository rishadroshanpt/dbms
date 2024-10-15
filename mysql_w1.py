import mysql.connector
con=mysql.connector.connect(user='roshan',host='localhost',password='rOsHaN..666',database='mysqlw1')
con.autocommit=True
cur=con.cursor()
# cur.execute("create database mysqlw1")
try:
    cur.execute("create table std (roll int,name text,age int)")
except:
    pass
l=int(input('Enter numner of students : '))
for i in range(l):
    roll=int(input('Enter roll no of the student : '))
    name=input('Enter name of the student : ')
    age=int(input('Enter age of the student : '))
    cur.execute("insert into std (roll,name,age)values(%s,%s,%s)",(roll,name,age))