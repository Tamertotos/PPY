from turtle import Turtle
class Country(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def move(self,country,x,y):
        self.goto(x,y)
        self.write(f"{country}",align="left", font=("Arial",8,"bold"))
