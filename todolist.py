from tkinter import *
def submit():
    food=[]
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    print("you have order")
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())
window=Tk()

listbox=Listbox(window,bg="blue",font=("constantai",35),width=12,selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"garlic bread")

listbox.config(height=listbox.size())
    
entryBox=Entry(window)
entryBox.pack()

submitButton=Button(window,text="submit",command=submit)
submitButton.pack()

addButton=Button(window,text="Add",command=add)
addButton.pack()

deleteButton=Button(window,text="Delete",command=delete)
deleteButton.pack()

window.mainloop()