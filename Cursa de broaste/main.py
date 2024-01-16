from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Bet who will win!",prompt="Bet the color!")
color=["red","yellow","blue","green","purple","orange"]
y=-70
x=-230
all_turtles=[]
for turtle_index in range(0,6):

    some = Turtle(shape= "turtle")
    some.color(color[turtle_index])
    some.penup()
    some.goto(x,y)
    y+=25
    all_turtles.append(some)
if user_input:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print("You win")
            else:
                print("You lost")   
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)



screen.exitonclick()