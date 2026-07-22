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
    guessed_countries = []
    while len(guessed_countries) < data.shape[0]:
        user_answer = screen.textinput(title=f" {len(guessed_countries)}/{data.shape[0]} Guess the country", prompt="What's another country's name?").title()
        if user_answer == "Exit":
            break
        if user_answer in countries and user_answer not in guessed_countries:
            x,y = data_loader.get_coordinates(data,user_answer)
            country = Country()
            country.move(country=user_answer,x=x,y=y)
            guessed_countries.append(user_answer)

    return guessed_countries

def main():
    screen = setup_screen()
    data = data_loader.arrange_data("europe_countries.csv")
    missed_countries = game_loop(screen,data)
    data_loader.create_csv(data,missed_countries)

if __name__ == "__main__":
    main()