from turtle import Turtle

MOVE = 30

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE)

    def down(self):
        self.goto(self.xcor(), self.ycor() - MOVE)
