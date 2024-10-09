import sqlite3
con = sqlite3.connect("task1.db")
try:
    con.execute("create table std(roll_no int,name text,age int)")
except:
    pass
l=int(input("enter no of students : "))
for i in range(l):
    roll=i+1
    name=input('Enter name : ')
    age=int(input('Enter age : '))
    con.execute("insert into std(roll_no,name,age)values(?,?,?)",(roll,name,age))
    con.commit()