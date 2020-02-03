import requests
from bs4 import BeautifulSoup

URL = 'https://automatetheboringstuff.com/2e/chapter0/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(class_='main')
print(results)