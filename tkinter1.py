# import tkinter

# win=tkinter.Tk()
# win.title('Hoooo')
# win.configure(bg='lime')
# win.minsize(250,250)
# win.maxsize(500,500)
# l1=tkinter.Label(win,text='Hello world',bg='lime')
# # l1.pack()
# # l1.place(x=50,y=50)
# l1.grid(row=0,column=0)


# l2=tkinter.Label(win,text='Hellooooo world',bg='lime')
# # l2.pack()
# # l2.place(x=50,y=50)
# l2.grid(row=1,column=1)

# win.mainloop()










import tkinter

win=tkinter.Tk()
win.title('Hoooo')
win.configure(bg='lime')
win.minsize(350,350)
win.maxsize(700,700)

def save():
    l4.configure(text=e1.get())
    l5.configure(text=e2.get())
    l6.configure(text=e3.get())


l1=tkinter.Label(win,text='Name',bg='lime')
l1.place(x=50,y=50)

e1=tkinter.Entry(win)
e1.place(x=150,y=50)



l2=tkinter.Label(win,text='Username',bg='lime')
l2.place(x=50,y=80)

e2=tkinter.Entry(win)
e2.place(x=150,y=80)



l3=tkinter.Label(win,text='Password',bg='lime')
l3.place(x=50,y=110)

e3=tkinter.Entry(win)
e3.place(x=150,y=110)

btn1=tkinter.Button(win,text='save',bg='grey',activebackground='black',activeforeground='grey',command=save)
btn1.place(x=150,y=150)

l4=tkinter.Label(win)
l4.place(x=150,y=180)

l5=tkinter.Label(win)
l5.place(x=150,y=210)

l6=tkinter.Label(win)
l6.place(x=150,y=240)

win.mainloop()