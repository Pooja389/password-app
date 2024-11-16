from tkinter import *
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 3
reps = 0

def start_timer():
    global reps
    reps += 1
    work_sec = 2*60
    short_break_Sec = SHORT_BREAK_MIN*60
    long_break_Sec = LONG_BREAK_MIN*60
    if reps%8 == 0:
        label.config(text = "LONG BREAK")
        countdown(long_break_Sec)
        exit()

    if reps%2 == 0:
        label.config(text = "SHORT BREAK")
        countdown(short_break_Sec)

    if reps%2 == 1:
        label.config(text = "WORK")
        countdown(work_sec)        
        
def countdown(count):
    count_min = int(count/60)
    count_sec = count%60

    if count_min > 9:
        if count_sec > 9:
            canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
        else:
            canvas.itemconfig(timer_text,text=f"{count_min}:0{count_sec}")
    else:
        if count_sec > 9:
            canvas.itemconfig(timer_text,text=f"0{count_min}:{count_sec}")
        else:
            canvas.itemconfig(timer_text,text=f"0{count_min}:0{count_sec}")    
    
    if count > 0:  
        window.after(1000, countdown, count - 1)
    else:
        start_timer()

def reset_timer():
    window.after_cancel(start_timer)
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="WORK", fg=GREEN)

window = Tk()
window.title("tomato timer")
window.minsize(height = 350,width = 350)
window.config(padx = 50, pady = 50)

canvas = Canvas(height= 250, width= 250)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(120,100,image = tomato_img)
timer_text = canvas.create_text(120,120,text="00:00",font = ("Arial",20,"normal"))
canvas.grid(row = 1,column=0,columnspan=2)

label = Label(text="TIMER",font=(FONT_NAME,20,"bold"))
label.grid(row = 0,column=0,columnspan=2)

button_s = Button(text="start",width=10,command=start_timer)
button_s.grid(row = 2,column=0)

button_r = Button(text = "reset",width=10,command=reset_timer)
button_r.grid(row = 2,column=1,columnspan=1)

window.mainloop()