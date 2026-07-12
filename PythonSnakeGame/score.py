from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,275)
        self.color("white")
        self.hideturtle()
        with open("highscore.txt") as file:
            self.highscore = int(file.read())
        self.score = 0

    def announce(self):
        self.clear()
        self.write(f"Score:  {self.score}  High Score:  {self.highscore}", align="center", font=("Arial",16,"bold"))

    def modify_high_score(self):
        if self.score > self.highscore:
            with open("highscore.txt",mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.announce()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 16, "bold"))

    def increase_score(self):
        self.score += 1
        self.announce()