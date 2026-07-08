from turtle import Turtle,Screen
from paddle import Paddle
from score import Score
from ball import Ball
import time

WIDTH = 1200
HEIGHT = 800

def setup_screen():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(WIDTH,HEIGHT)
    screen.title("Pong")
    screen.tracer(0)
    screen.listen()

    return screen

def draw_line():
    line = Turtle("square")
    line.color("white")
    line.pensize(5)
    xcor = 0
    ycor = 400
    line.hideturtle()
    line.penup()
    line.goto(0,400)
    for i in range(40):
        if i % 2 == 0:
            line.pendown()
        else:
            line.penup()
        line.goto(xcor, ycor := ycor - 20)

def game_loop(screen,user1,user2,score,ball):
    while True:
        score.announce()


        ball.move()
        if abs(ball.ycor()) > 380:
            ball.bounce_ycor()

        if ball.distance(user1) < 40 and ball.xcor() > 560 or ball.distance(user2) < 40 and ball.xcor() < -560:
            ball.bounce_xcor()

        if ball.xcor() > 610:
            score.l_point()
            ball.reset()

        if ball.xcor() < -610:
            score.r_point()
            ball.reset()

        time.sleep(0.01)
        screen.update()

def main():
    screen = setup_screen()
    user1 = Paddle((570,80))
    user2 = Paddle((-570,80))
    score = Score()
    ball = Ball(7,7)
    draw_line()


    screen.onkeypress(user1.up, "Up")
    screen.onkeypress(user1.down, "Down")
    screen.onkeypress(user2.up, "w")
    screen.onkeypress(user2.down, "s")
    game_loop(screen,user1,user2,score,ball)

    screen.exitonclick()

if __name__ == "__main__":
    main()