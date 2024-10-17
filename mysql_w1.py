import mysql.connector
con=mysql.connector.connect(user='roshan',host='localhost',password='rOsHaN..666',database='mysqlw1')
con.autocommit=True
cur=con.cursor()
# cur.execute("create database mysqlw1")
try:
    cur.execute("create table std (roll int,name text,age int)")
except:
    pass
# l=int(input('Enter numner of students : '))
# for i in range(l):
#     roll=int(input('Enter roll no of the student : '))
#     name=input('Enter name of the student : ')
#     age=int(input('Enter age of the student : '))
#     cur.execute("insert into std (roll,name,age)values(%s,%s,%s)",(roll,name,age))
# cur.execute("select * from std order by name desc")
cur.execute("select * from std where name like '_k%'")
data=cur.fetchall()
for i in data:
    print(i)
# try:
#     cur.execute("create table mark (roll_no int,sub text,mark int)")
# except:
#     pass
# cur.execute("insert into mark(roll_no,sub,mark)values(1,'cs',70),(1,'chem',49),(2,'phy',58),(4,'eng',45)")
# cur.execute("select std.roll_no,std.name,std.age,mark.sub,mark.mark from std cross join mark")
# data=cur.fetchall()
# for i in data:
#     print(i)
# cur.execute("select name,count(age) from std group by name")
# data=cur.fetchall()
# for i in data:
#     print(i)