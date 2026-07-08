from turtle import Turtle

class Ball(Turtle):
    def __init__(self,dx,dy):
        super().__init__()
        self.shape("circle")
        self.shapesize(1,1)
        self.color("green")
        self.penup()
        self.dx = dx
        self.dy = dy

    def move(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)