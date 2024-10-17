import tkinter

win=tkinter.Tk()
win.title('Hoooo')
win.configure(bg='lime')
win.minsize(350,350)
win.maxsize(700,700)

def reg():
    win=tkinter.Tk()
    win.title('Hoooo')
    win.configure(bg='lime')
    win.minsize(350,350)
    win.maxsize(700,700)


    l1=tkinter.Label(win,text='Register',bg='lime')
    l1.place(x=150,y=20)

    l2=tkinter.Label(win,text='Username',bg='lime')
    l2.place(x=50,y=80)

    e2=tkinter.Entry(win)
    e2.place(x=150,y=80)



    l3=tkinter.Label(win,text='Password',bg='lime')
    l3.place(x=50,y=110)

    e3=tkinter.Entry(win)
    e3.place(x=150,y=110)

    btn1=tkinter.Button(win,text='Register',bg='grey',activebackground='black',activeforeground='grey')
    btn1.place(x=150,y=150)

    win.mainloop()

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

btn1=tkinter.Button(win,text='Login',bg='grey',activebackground='black',activeforeground='grey')
btn1.place(x=150,y=150)

btn2=tkinter.Button(win,text='Register',bg='grey',activebackground='black',activeforeground='grey',command=reg)
btn2.place(x=150,y=180)

win.mainloop()