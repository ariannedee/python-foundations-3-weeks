import requests

URL = 'https://github.com/ariannedee/python-foundations-3-weeks'

# Dictionary of HTTP headers
headers = {'User-Agent': f'Your name (your@email.com)'}

# Dictionary of URL parameters
params = {'key1': 'value1', 'key2': 'value2'}  # Gets appended to url: {url}?key1=value1&key2=value2
response = requests.get(URL, headers=headers, params=params)

# Full list of HTTP status codes: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
# Common status codes:
# - 200 OK
# - 401 Unauthorized
# - 404 Not found
# - 502 Bad gateway
print(response.status_code)

# Raise an exception if the request was unsuccessful
response.raise_for_status()

# Get text contents
print(response.text)

with open('data/google.html', 'w', encoding="utf-8") as file:
    file.write(response.text)
