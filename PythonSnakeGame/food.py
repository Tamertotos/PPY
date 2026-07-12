from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("green")
        self.penup()
        self.shapesize(0.5,0.5,1)
        self.goto(100,100)

    def move(self):
        self.goto(randint(-280,280),randint(-280,280))
