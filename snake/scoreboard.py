from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.HighScore = 0
        self.goto(0,260)
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_score()
        
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore:{self.HighScore}",align="center",font=("Arial",24,"normal"))
        
    def increase_score(self):
        self.score+=1
        self.update_score()
        
        
    def reset(self):
        if self.score>self.HighScore:
            self.HighScore = self.score
        self.score = 0
        self.update_score()
        
    """def game_over(self):
        self.goto(0,0)
        self.write("Game over",align="center",font=("Arial",24,"normal"))"""
        
    def reset(self):
        if self.score > self.HighScore:
            self.HighScore = self.score
        self.score = 0
        self.update_score()        
        
    
