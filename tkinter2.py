import tkinter
import sqlite3
# con=sqlite3.connect('dbms/tkinterSample.db')
# con.execute('create table sample(uname text,passwd text)')
win=tkinter.Tk()
win.title('Hoooo')
win.configure(bg='lime')
win.minsize(350,350)
win.maxsize(700,700)

def home():
    win2=tkinter.Tk()
    win2.configure(bg='lime')
    win2.minsize(350,350)
    win2.maxsize(700,700)
    l1=tkinter.Label(win2,text='Home Page',bg='lime')
    l1.place(x=150,y=20)
    btn1=tkinter.Button(win2,text='Logout',command=win2.quit)
    btn1.place(x=150,y=150)
    win2.mainloop()

def login():
    con=sqlite3.connect('dbms/tkinterSample.db')
    data=con.execute('select * from sample')
    f=0
    for i in data:
        if i[0]==e2.get() and i[1]==e3.get():
            f=1
            home()
    if f==0:
        l4.config(text='Invalid username or password')

def reg_form():
    win1=tkinter.Tk()
    win1.title('Hoooo')
    win1.configure(bg='lime')
    win1.minsize(350,350)
    win1.maxsize(700,700)

    def reg():
        con=sqlite3.connect('dbms/tkinterSample.db')
        con.execute('insert into sample(uname,passwd)values(?,?)',(e2.get(),e3.get()))
        con.commit()
        win1.destroy()
        
    l1=tkinter.Label(win1,text='Register',bg='lime')
    l1.place(x=150,y=20)

    l2=tkinter.Label(win1,text='Username',bg='lime')
    l2.place(x=50,y=80)

    e2=tkinter.Entry(win1)
    e2.place(x=150,y=80)



    l3=tkinter.Label(win1,text='Password',bg='lime')
    l3.place(x=50,y=110)

    e3=tkinter.Entry(win1)
    e3.place(x=150,y=110)

    btn1=tkinter.Button(win1,text='Register',bg='grey',activebackground='black',activeforeground='grey',command=reg)
    btn1.place(x=150,y=150)

    win1.mainloop()

l1=tkinter.Label(win,text='Login',bg='lime')
l1.place(x=150,y=20)

l2=tkinter.Label(win,text='Username',bg='lime')
l2.place(x=50,y=80)

e2=tkinter.Entry(win)
e2.place(x=150,y=80)



l3=tkinter.Label(win,text='Password',bg='lime')
l3.place(x=50,y=110)

e3=tkinter.Entry(win)
e3.place(x=150,y=110)

btn1=tkinter.Button(win,text='Login',bg='grey',activebackground='black',activeforeground='grey',command=login)
btn1.place(x=150,y=150)

btn2=tkinter.Button(win,text='Register',bg='grey',activebackground='black',activeforeground='grey',command=reg_form)
btn2.place(x=150,y=180)

l4=tkinter.Label(win)
l4.place(x=100,y=210)

win.mainloop()