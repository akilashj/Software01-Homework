import requests

try:
    response = requests.get("https://api.chucknorris.io/jokes/random")
    if response.status_code == 200:
        data = response.json()
        print(data['value'])

except requests.exceptions.RequestException as e:
    print("Request could not be completed:")