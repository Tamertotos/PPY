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

    def bounce_ycor(self):
        self.dy *= -1

    def bounce_xcor(self):
        self.dx *= -1

    def reset(self):
        self.goto(0,0)
        self.bounce_xcor()