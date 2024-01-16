from turtle import Turtle,Screen 
timmy = Turtle()
timmy.shape("circle")
timmy.color("red")
def curve():
    for i in range(200):
        timmy.right(1)
        timmy.forward(1)
def heart():
    timmy.fillcolor('red')
    timmy.begin_fill()
    timmy.left(140)
    timmy.forward(113)
    curve()
    timmy.left(120)
    curve()
    timmy.forward(112)
    timmy.end_fill()
heart()
screen = Screen()
screen.exitonclick()