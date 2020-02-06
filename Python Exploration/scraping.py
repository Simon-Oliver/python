import requests
from bs4 import BeautifulSoup

URL = 'https://www.internetlivestats.com/watch/websites/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(class_='rts-counter')
num1 = soup.find(id='innercounterview-desc')
num2 = num1.find('a')

print(num2.text)
