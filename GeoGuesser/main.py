import turtle
import data_loader
from country import Country

def setup_screen():
    screen = turtle.Screen()
    screen.title("Europe country guessing game")
    screen.bgpic("europe.gif")
    screen.setup(800,750)
    return screen

def game_loop(screen,data):
    countries = data.country.to_list()
    score = 0
    while True:
        user_answer = screen.textinput(title=f" {score}/{data.shape[0]} Guess the country", prompt="What's another country's name?").lower()
        if user_answer in countries:
            x,y = data_loader.get_coordinates(data,user_answer)
            country = Country()
            country.move(country=user_answer,x=x,y=y)
            score += 1

def main():
    screen = setup_screen()
    data = data_loader.arrange_data("europe_countries.csv")
    game_loop(screen,data)
    screen.exitonclick()

if __name__ == "__main__":
    main()