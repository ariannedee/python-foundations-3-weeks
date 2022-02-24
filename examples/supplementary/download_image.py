import requests
import shutil

URL = "https://www.python.org/static/community_logos/python-logo.png"
response = requests.get(URL, stream=True)

response.raise_for_status()

if response.status_code == 200:
    with open('data/python.png', 'wb') as f:
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, f)
