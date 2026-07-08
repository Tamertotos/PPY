from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0

    def announce(self):
        self.clear()
        self.goto(-50,360)
        self.write(f"{self.left_score}", align="center", font=("Arial",24,"bold"))
        self.goto(50,360)
        self.write(f"{self.right_score}", align="center", font=("Arial",24,"bold"))

    def l_point(self):
        self.left_score += 1

    def r_point(self):
        self.right_score += 1