from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"









# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Cards")
#window.config(padx=50,pady=50,bg=card_back_photo)


canvas = Canvas(height=400,width=400)
card_back_photo = PhotoImage(file="card_back.png")
window.config(padx=50,pady=50,bg=card_back_photo)

#Entry
right_photo = PhotoImage(file="right.png")
right_button = Button(image=right_photo)
right_button.grid(row=1,column=0)

wrong_photo = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_photo)
wrong_button.grid(row=1,column=1)




window.mainloop()


