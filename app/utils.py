import requests


def fetch_url(url):
    response = requests.get(url)
    return response.text
