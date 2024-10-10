import sqlite3
con = sqlite3.connect("dbms/work1.db")
try:
    con.execute("create table std(roll_no int,name text,age int)")
except:
    pass
# con.execute("insert into std(roll_no,name,age)values(1,'marco',16),(2,'eldhose',15)")
# con.commit()
# roll=int(input('Enter roll no : '))
# name=input('Enter name : ')
# age=int(input('Enter age : '))
# con.execute("insert into std(roll_no,name,age)values(?,?,?)",(roll,name,age))
# con.commit()
# roll=int(input('Enter roll no of student that you want to select : '))
# data=con.execute("select * from std where roll_no=?",(roll,))
# for i in data:
#     print(i)
# name=input('Enter name : ')
# data=con.execute("update std set name='marco paulo',age=17 where name=?",(name,))
# con.commit()
# l=int(input("enter no of students : "))
# for i in range(l):
#     roll=i+1
#     name=input('Enter name : ')
#     age=int(input('Enter age : '))
#     con.execute("insert into std(roll_no,name,age)values(?,?,?)",(roll,name,age))
#     con.commit()
# no=int(input('Enter no : '))
# con.execute("delete from std where roll_no=?",(no,))
# con.commit()
# data=con.execute("select * from std where name like '%a_'")
# for i in data:
#     print(i)
data=con.execute("select * from std order by name desc")
for i in data:
    print(i)