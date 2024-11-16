from tkinter import *
import pandas,random
window = Tk()
window.title("flash card")
window.minsize(height = 600,width = 750)
window.config(bg = "#B1DDC6")

canvas = Canvas(height=500,width=900)
image_front_card = PhotoImage(file="card_front.png")
image_back_card = PhotoImage(file="card_back.png")
image_right = PhotoImage(file="right.png")
image_wrong = PhotoImage(file = "wrong.png")

data = pandas.read_csv("french_words.csv")
to_learn = data.to_dict(orient = "records")

current_card = {}

def next_word():
    global flip_timer,current_card

    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    rand_french_word = current_card["French"]
    canvas.itemconfig(card_image,image = image_front_card)
    canvas.itemconfig(card_text,text = rand_french_word)
    canvas.itemconfig(title,text = "French")
    flip_timer = window.after(3000,flip) 
    
    
def flip():
    global current_card
    eng_word = current_card["English"]
    canvas.itemconfig(title,text = "English")
    canvas.itemconfig(card_image,image = image_back_card)
    canvas.itemconfig(card_text,text = eng_word)

def is_known():
    global current_card
    to_learn.remove(current_card)
    updated_data = pandas.DataFrame(to_learn)
    updated_data.to_csv("french_words.csv", index=False)    
    next_word()


flip_timer = window.after(3000,flip)    

card_image = canvas.create_image(450,250,image = image_front_card)
title = canvas.create_text(450,100,text="", font=("Arial",40,"italic"), fill="black")
card_text = canvas.create_text(450,225,text="",font=("Arial",32,"normal"), fill="black")
canvas.config(bg="#B1DDC6",highlightthickness=0)
button_r = Button(image=image_right,command=is_known)
button_r.grid(row = 1,column=0)

button_w = Button(image = image_wrong,command=next_word)
button_w.grid(row = 1,column = 1)

canvas.grid(row = 0, column = 0,pady=20,columnspan=2)
next_word()

window.mainloop()



