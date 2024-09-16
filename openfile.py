from tkinter import *
from tkinter import filedialog

def openFile():
     #filepath = filedialog.askopenfilename()
     filepath=filedialog.askopenfilename(initialdir=r"  C:\Users\kalar\OneDrive\Desktop",
                                         title="open tne file",
                                         filetypes=(("textfiles","*.txt"),("All files",".*")))
     
     file=open(filepath,"r")
     print(file.read())
     file.close()
     
window=Tk()
button=Button(text="open",command=openFile)
button.pack()
window.mainloop()