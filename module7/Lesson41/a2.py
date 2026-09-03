from tkinter import *
from tkinter import messagebox
window = Tk()

# window.title('')
window.geometry('500x500')


def display():
    # messagebox.geometry("10x10")
    messagebox.showwarning("Alert,Virus Found")


Btn = Button(text='Scan for virus', command=display,
             height='1', bg='black', fg='white')

Btn.place(x=200, y=215)
window.mainloop()
