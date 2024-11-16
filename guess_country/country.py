from turtle import *
screen = Screen()
import pandas

turtle = Turtle()
image = "blank_states_img.gif" 
screen.title("US states game")
screen.addshape(image)
turtle.shape(image)

write_name = Turtle()
write_name.pencolor("red")
write_name.penup()
write_name.hideturtle()

data = pandas.read_csv("data20.csv")
state_list = data.state.to_list()
x_cor = data.x.to_list()
y_cor = data.y.to_list()

val = 0
lives = 50
while lives > 0:
    ask = screen.textinput(title=f"{val}/50 states correct",prompt=f"guess a state, your lives {lives}").title()
    if ask in state_list:
        val += 1
    for i in range(len(state_list)):
        if state_list[i] == ask:
            write_name.goto(x_cor[i],y_cor[i])
            write_name.write(ask, font = ("Arial",12,"bold"))
    lives -= 1    
screen.exitonclick()