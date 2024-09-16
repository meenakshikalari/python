from tkinter import*
from tkinter import ttk

window=Tk()
notebook=ttk.Notebook(window)

tab1=Frame(notebook)
tab2=Frame(notebook)
tab3=Frame(notebook)
tab4=Frame(notebook)
notebook.add(tab1,text="tab1")
notebook.add(tab2,text="tab2")
notebook.add(tab3,text="tab3")
notebook.add(tab4,text="tab4")
notebook.pack(expand=True,fill="both")

Label(tab1,text="hello, this is tab1",width=50,height=25).pack()
Label(tab2,text="goodbye,this is the tab2", width=50,height=25).pack()
Label(tab3,text="this is the tab3 and hi good morning once agin", width=50,height=25).pack()
Label(tab4,text="this is the tab 4", width=50,height=25).pack()
window.mainloop()