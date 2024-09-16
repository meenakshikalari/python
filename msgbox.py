from tkinter import *
from tkinter import messagebox

def click():
    messagebox.showinfo(title="this is the an info msg box",message="you are the person")
    if messagebox.askokcancel(title="ask to cancel",message="do u want to cancel"):
        print("you did the thing")
    else:
        print("you canceled the thing")

window=Tk()
button=Button(window,command=click,text="click me")
button.pack()
window.mainloop()