from time import strftime
from tkinter import *

window = Tk()
window.title("Clock")

def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000,time)

label = Label(window,font=("ds-digital",80),background="black",foreground="cyan")
label.pack(anchor="center")
time()
window.mainloop()