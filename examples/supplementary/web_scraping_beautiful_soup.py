"""
Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""
from bs4 import BeautifulSoup
import requests

URL = "https://google.com"

response = requests.get(URL)
html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser')
buttons = soup.find_all('input', attrs={'type': 'submit'})
for button in buttons:
    print(button.get('value'))
