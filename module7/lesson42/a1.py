from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()

window.title('Text Editor')
window.geometry('600x500')
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)


textwindow = Text(window)
frbutton = Frame(window, relief=RAISED, bd=2)


def openfile():
    """Open a file for editing."""
    filepath = asksaveasfilename(
        filetypes=[("Text Files", "*.txt"), ("ALL Files", "*.*")])
    if not filepath:
        return
    textwindow.delete(1.0, END)
    with open(filepath, "r") as input_file:

        text = input_file.read()

        textwindow.insert(END, text)
        input_file.close()
    window.title(f"Codingal Text editor - {filepath}")


def saveas():
    filepath = asksaveasfilename(
        filetypes=[("Text Files", "*.txt"), ("ALL Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = textwindow.get(1.0, END)
        output_file.write(text)
    window.title(f"Codingal Text editor - {filepath}")


Btn = Button(frbutton, text='Open', command=openfile, bg='black', fg='white')
Btn1 = Button(frbutton, text='Save As', bg='black', fg='white', command=saveas)

Btn.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
Btn1.grid(row=1, column=0, sticky="ew", padx=5)
frbutton.grid(row=0, column=0, sticky="ns")
textwindow.grid(row=0, column=1, sticky="nsew")


window.mainloop()
