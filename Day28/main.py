from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    #00:00
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    #it it's the multiple 8th rep
    if reps%8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
        
    #if it's the 1st/3rd/5th/7th reps
    elif reps%2 == 1:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
        
    #if it's 2nd/4th/6th rep
    else: 
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
# ---------------------------- COUNTDOWN MECHANISM 
# ------------------------------- # 
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = reps//2
        for _ in range(work_sessions):
            mark += "✓"
        check_marks.config(text=mark)
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Timer label
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=("Roboto", 24, "bold"))
title_label.grid(row=0, column=1)

#canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)


#start label
start_label = Button(text="Start", command=start_timer, highlightthickness=0)
start_label.grid(row=2, column=0)

#reset label
reset_label = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_label.grid(row=2, column=2)

#checkmarks
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)
window.mainloop()