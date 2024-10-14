# import sqlite3
# con = sqlite3.connect("dbms/task1.db")
# try:
#     con.execute("create table std(roll_no int,name text,age int)")
# except:
#     pass
# l=int(input("enter no of students : "))
# for i in range(l):
#     roll=i+1
#     name=input('Enter name : ')
#     age=int(input('Enter age : '))
#     con.execute("insert into std(roll_no,name,age)values(?,?,?)",(roll,name,age))
#     con.commit()
# data=con.execute("select name from std")
# for i in data:
#     print(i)









import sqlite3
con = sqlite3.connect("dbms/mark.db")
try:
    con.execute("create table std(roll_no int,name text,age int)")
    con.execute("create table mark(roll_no int,sub text,mark int)")
except:
    pass
# l=int(input('Enter no of students : '))
# for i in range(l):
#     roll_no=i+1
#     name=input('Enter name : ')
#     age=int(input('Enter age : '))
#     con.execute("insert into std(roll_no,name,age)values(?,?,?)",(roll_no,name,age))
#     con.commit()
# con.execute("insert into mark(roll_no,sub,mark)values(1,'cs',70),(1,'chem',49),(2,'phy',58),(4,'eng',45)")
# con.commit()
# data=con.execute("select std.roll_no,std.name,std.age,mark.sub,mark.mark from std cross join mark")
# for i in data:
#     print(i)
data=con.execute("select name,count(age) from std group by name")
for i in data:
    print(i)