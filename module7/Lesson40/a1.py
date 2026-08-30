from tkinter import *

window = Tk()

window.title('Geometry')
window.geometry('700x700')


nums = [[9, 8, 7], [6, 5, 4], [3, 2, 1], ['#', 0, '*']]

for i in range(4):
    window.columnconfigure(i, weight=1, minsize=200)
    window.rowconfigure(i, weight=1, minsize=150)
    for j in range(0, 3):
        frame = Frame(master=window, relief=SUNKEN, borderwidth=1)
        frame.grid(row=i, column=j)
        label = Label(master=frame, text=nums[i][j], bg='blue')
        label.pack(padx=6, pady=6)


window.mainloop()
