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

def game_loop(screen,user1,user2,user1_score,user2_score,ball):
    while True:
        user1_score.announce()
        user2_score.announce()


        ball.move()
        if abs(ball.ycor()) > 370:
            ball.dy *= -1

        if ball.xcor() > 610:
            user2_score.score +=1
            ball.goto(0,0)

        if ball.xcor() < -610:
            user1_score.score +=1
            ball.goto(0,0)

        if  ball.distance(user1) < 40:
            ball.dx *= -1

        if  ball.distance(user2) < 40:
            ball.dx *= -1

        if user2_score.score == 3:
            user2_score.announce_winner()
            break

        if user1_score.score == 3:
            user1_score.announce_winner()
            break


        screen.update()
        time.sleep(0.05)

def main():
    screen = setup_screen()
    user1 = Paddle(570,80)
    user2 = Paddle(-570,80)
    score1 = Score((30,360), "user1")
    score2 = Score((-30,360) , "user2")
    ball = Ball(10,10)
    draw_line()


    screen.onkeypress(user1.up, "Up")
    screen.onkeypress(user1.down, "Down")
    screen.onkeypress(user2.up_w, "w")
    screen.onkeypress(user2.down_s, "s")
    game_loop(screen,user1,user2,score1,score2,ball)

    screen.exitonclick()

if __name__ == "__main__":
    main()