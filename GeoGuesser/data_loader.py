import pandas

def arrange_data(path):
    data = pandas.read_csv(path)
    data["country"] = data.country.str.lower()
    return data

def get_coordinates(data,guess):
    country_x = data[data["country"] == guess].x.iloc[0]
    country_y = data[data["country"] == guess].y.iloc[0]
    return country_x,country_y

