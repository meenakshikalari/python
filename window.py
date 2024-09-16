""" from tkinter import *
def create_window():
    #new_window = Topleve()
    new_window = Tk()

    old_window.destroy()


#window = Tk()
old_window = Tk()
#Button(window,text="create new window",command=create_window).pack()
Button(old_window,text="create new window",command=create_window).pack()
#window.mainloop()
old_window.mainloop() """


from tkinter import *
def create_window():
    # new_window = Toplevel()
    new_window=Tk()
  
    old_window.destroy()
# window=Tk()
old_window=Tk()
# Button(window,text="create new window",command=create_window).pack()
Button(old_window,text="create new window",command=create_window).pack()
old_window.mainloop()
