import turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.create_initial_snake()
        self.head = self.segments[0]

    def create_initial_snake(self):
        xcor = 0
        for i in range(3):
            self.add_segments(xcor := xcor -20,0)

    def add_segments(self,x_position,y_position):
        snake = turtle.Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(x_position, y_position)
        self.segments.append(snake)

    def extend(self):
        self.add_segments(self.segments[-1].xcor(),self.segments[-1].ycor())

    def move(self):
        '''Every subsequent segment follows the prior segment'''
        for i in range(len(self.segments) -1,0,-1):
            xcor = self.segments[i - 1].xcor()
            ycor = self.segments[i - 1].ycor()
            self.segments[i].goto(xcor,ycor)
        self.head.forward(20)

    def collide_tail(self):
        for i in self.segments[:0:-1]:
            if self.head.distance(i) < 15:
                return True
        else:
            return False

    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.create_initial_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)