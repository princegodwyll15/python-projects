# frontend.py
import requests
def send_greeting_request(name):
    url = 'http://localhost:5000/api/greet'
    response = requests.get(url)
    return response.json()