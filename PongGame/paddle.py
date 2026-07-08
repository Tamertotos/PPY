from turtle import Turtle

MOVE = 20

class Paddle(Turtle):

    def __init__(self,xcor,ycor):
        super().__init__()
        self.xcor = xcor
        self.ycor = ycor
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(xcor, ycor := ycor - 20)

    def up(self):
        self.ycor += 20
        self.goto(self.xcor, self.ycor)

    def down(self):
        self.ycor -= 20
        self.goto(self.xcor, self.ycor)


    def up_w(self):
        self.ycor += 20
        self.goto(self.xcor, self.ycor)


    def down_s(self):
        self.ycor -= 20
        self.goto(self.xcor, self.ycor)
