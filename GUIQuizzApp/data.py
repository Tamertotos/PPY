import requests

PARAMETERS = {
    "amount":15,
    "category":15,
    "difficulty":"easy",
    "type":"boolean"
}

def get_questions_api(url):
    response = requests.get(url, params=PARAMETERS)
    data = response.json()["results"]

    return data
