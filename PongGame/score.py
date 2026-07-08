from turtle import Turtle

class Score(Turtle):
    def __init__(self,position,name):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.score = 0
        self.name = name


    def announce(self):
        self.clear()
        self.write(f"{self.score}", align="center", font=("Arial",24,"bold"))

    def announce_winner(self):
        self.goto(0,0)
        self.write(f"THE WINNER IS {self.name} with {self.score}", align="center", font=("Arial", 24, "bold"))

