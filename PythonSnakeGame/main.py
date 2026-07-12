from snake import Snake
import turtle
from food import Food
from score import Score
import time

WIDTH, HEIGHT = 600,600

def setup_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.bgcolor("black")
    screen.tracer(0)
    screen.listen()
    return screen


def game_loop(screen, snake, food, score):
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        score.announce()
        snake.move()

        if snake.head.distance(food) < 15:
            food.move()
            score.increase_score()
            snake.extend()

        if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
            snake.reset()
            score.modify_high_score()
            score.game_over()
            game_is_on = False

        if snake.collide_tail():
            snake.reset()
            score.modify_high_score()
            score.game_over()
            game_is_on = False

def main():
    screen = setup_screen()
    snake = Snake()
    food = Food()
    score = Score()

    screen.onkeypress(snake.up,"Up")
    screen.onkeypress(snake.left,"Left")
    screen.onkeypress(snake.down,"Down")
    screen.onkeypress(snake.right,"Right")

    game_loop(screen, snake,food,score)
    screen.exitonclick()

if __name__ == "__main__":
    main()