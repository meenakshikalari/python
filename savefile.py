from tkinter import *
from tkinter import filedialog
def savefile():
    file=filedialog.asksaveasfile(defaultextension='.txt',
                                  filetypes=[("Textf file","txt"),
                                             ("html file",".html"),
                                             ("all files","*"),
                                             ])
    if file is None:
        return
    filetext=str(text.get(1.0,END))

    file.write(filetext)
    file.close()

window=Tk()
button=Button(window,text="save",command=savefile)
button.pack()
text=Text(window)
text.pack()
window.mainloop()