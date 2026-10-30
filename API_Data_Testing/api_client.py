import requests

API_URL = "https://jsonplaceholder.typicode.com/users"


def fetch_users():
    response = requests.get(API_URL, timeout=10)

    response.raise_for_status()

    users = response.json()

    if not isinstance(users, list):
        raise ValueError("Expected the API to return a list of users.")

    return users