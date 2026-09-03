import requests

PARAMETERS = {
    "amount":15,
    "category":15,
    "difficulty":"easy",
    "type":"boolean"
}

def get_questions_api(url: str):
    """
    Returns the questions from a website

    Parameter:
        is the url of the webpage whereby there are questions we can retrieve via api call
    Returns:
           a list of dictionaries with questions in it.
    """

    response = requests.get(url, params=PARAMETERS)
    response.raise_for_status()
    data = response.json()["results"]

    return data
