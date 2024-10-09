import sqlite3
con = sqlite3.connect("work1.db")
try:
    con.execute("create table std(roll_no int,name text,age int)")
except:
    pass
# con.execute("insert into std(roll_no,name,age)values(1,'marco',16),(2,'eldhose',15)")
# con.commit()
roll=int(input('Enter roll no : '))
name=input('Enter name : ')
age=int(input('Enter age : '))
con.execute("insert into std(roll_no,name,age)values(?,?,?)",(roll,name,age))
con.commit()