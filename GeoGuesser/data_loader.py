import pandas

def arrange_data(path):
    data = pandas.read_csv(path)
    return data

def get_coordinates(data,guess):
    country_x = data[data["country"] == guess].x.item()
    country_y = data[data["country"] == guess].y.item()
    return country_x,country_y

def create_csv(data,guessed_countries):
    countries_to_learn = [country for country in data.country if country not in guessed_countries]
    if len(countries_to_learn) < data.shape[0]:
        df = pandas.DataFrame(countries_to_learn)
        df.to_csv("missed_ones.csv")
    else:
        print("You guessed every country correctly!")