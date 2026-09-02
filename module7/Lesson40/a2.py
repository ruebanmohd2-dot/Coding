from tkinter import *

window = Tk()

window.title('Login App')
window.geometry('800x350')

frame = Frame(master=window, relief=SUNKEN, borderwidth=1,
              height=200, width=325, bg='lightblue')


label1 = Label(frame, text='Full Name', fg='black',
               bg='yellow', height='1', width='12')
label2 = Label(frame, text='Email ID', fg='black',
               bg='yellow', height='1', width='12')
label3 = Label(frame, text='Enter Password', fg='black',
               bg='yellow', height='1', width='12')


name_entry = Entry(frame)
email_entry = Entry(frame)
password_entry = Entry(frame)


def display():
    name = name_entry.get()
    global message
    message = 'Congragulation On your new account'+"\n"
    greet = "Hello "+name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)


Btn = Button(text='Create Account', command=display,
             height='1', bg='black', fg='white')

text_box = Text(height=3)

frame.place(x=225, y=0)
label1.place(x=20, y=20)
label2.place(x=20, y=80)
label3.place(x=20, y=140)

name_entry.place(x=150, y=20)
email_entry.place(x=150, y=80)
password_entry.place(x=150, y=140)

Btn.place(x=325, y=210)
text_box.place(x=75, y=250)

window.mainloop()
