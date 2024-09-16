from tkinter import *
from tkinter.ttk import*
import time

def start():
    GB=100
    download=0
    speed=2
    while download < GB:
        time.sleep(0.05)
        bar['value']+=(speed/GB)*100
        download+=speed
        percent.set(f"{int((download/GB)*100)}%")
        text.set(f"{download}/{GB}gb completed")
        window.update_idletasks()


window=Tk()
percent=StringVar()
text=StringVar()
bar=Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)
percentLabel=Label(window,textvariable=percent).pack()
taskLabel=Label(window,textvariable=text).pack()
button=Button(window,text="download",command=start).pack()

percent.set("0%")
text.set("0/100 GB complted")

window.mainloop()