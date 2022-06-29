from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

#Label
my_label = Label(text="I am a Label",font=("Arial",12,"bold"))


my_label.config(text="New Text")
my_label.grid(column=0,row=0)

# Button 

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me",command=button_clicked)
button.grid(column=2,row=2)

new_button = Button(text="Click Me2")
new_button.grid(column=3,row=1)


# Entry

input = Entry(width=10)
print(input.get())
input.grid(column=3,row=2)


window.mainloop()