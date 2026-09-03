from tkinter import *

window = Tk()

window.title('Event Handler')
window.geometry('500x500')


def keypress(event):
    print(event.char)


def click(event):
    print("Button Was clicked")


Btn = Button(text='Click', height='1', bg='black', fg='white')


Btn.bind("<Button-1>", click)
window.bind("<Key>", keypress)
Btn.pack()
window.mainloop()
