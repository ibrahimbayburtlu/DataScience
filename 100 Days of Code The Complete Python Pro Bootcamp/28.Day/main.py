from _tkinter import *
from cgitb import reset, text
from tabnanny import check
import threading
from tkinter import Button, Canvas, Label, PhotoImage, Tk
from tracemalloc import start
from turtle import bgcolor, title
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():

    global reps
    reps += 1 
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60 

    if reps % 2 == 1:
        count_down(work_sec)
        title_label.config(text="Work",fg=GREEN)
    elif reps == 8:
        count_down(long_break_sec)
        title_label.config(text="Break",fg=RED)
    else:
        count_down(short_break_sec)
        title_label.config(text="Break",fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_min = count // 60
    count_sec = count % 60 
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    print(count)
    if count > 0:
        window.after(1000,count_down,count-1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodro")
window.config(padx=100,pady=50,bg=YELLOW)



title_label = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME, 50))
title_label.grid(column=1,row=0)


canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_ing = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_ing)
timer_text = canvas.create_text(103,112,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

start_timer()

start_button = Button(text="start")
start_button.grid(column=0,row=2)



reset_button = Button(text="reset")
reset_button.grid(column=2,row=2)


check_marks = Label(text="✔",fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=3)


window.mainloop()

