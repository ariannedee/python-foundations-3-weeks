import requests

base_url = f'https://api.openweathermap.org/data/2.5/onecall'


params = {
}

headers = {
    'content-type': 'application/json'
}

response = requests.get(base_url, headers=headers, params=params)

weather = response.json()['daily'][0]

