from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Welcome to snake")
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.down,"Down")
screen.onkey(snake.up,"Up")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.20)
    
    
    snake.move()
    
    if snake.head.distance(food)<12:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    
    
    
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-280:
        scoreboard.reset()
        snake.reset()
        
    for segment in snake.segment[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()
        
        


screen.exitonclick()


















