from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1#25
SHORT_BREAK_MIN = 0.5#5
LONG_BREAK_MIN = 2#20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(time_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
    #timer_text = 00:00
    #title_label "Timer"
    #reset check_marks

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
#    count_down(5)
    global reps  
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    remainder = reps % 8
    #If it is the 1st/3rd/5th/7th rep do 25 mins count down
    if remainder == 1 or remainder == 3 or remainder == 5 or remainder == 7: 
        count_down(work_sec) 
        timer_label.configure(text="Work", fg=GREEN)

    #If it is 8th rep count 25 minutes long break 
    if remainder == 0:
        timer_label.configure(text="Break", fg=RED)
        count_down(long_break_sec) 
         
    #if it is 2nd/4th/6th break count to short break
    if remainder == 2 or remainder == 4 or remainder == 6:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 10:
        count_sec == f"0{count_sec}"

    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer 
        timer = window.after(100, count_down, count - 1)
    else:
        start_timer() 
        mark = ""

        for _ in range(math.floor(reps/2)):
            mark += "✔" 
        check_mark.config(text=mark) 
         
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 28, "normal"), highlightthickness=0, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, highlightbackground=YELLOW, border=0, command=start_timer)
start_button.grid( column=0, row=2)
#timer_label.destroy()
reset_button = Button(text="Reset", highlightthickness=0, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW, highlightthickness=0)
check_mark.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)




window.mainloop()