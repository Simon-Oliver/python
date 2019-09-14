from requests import get
from bs4 import BeautifulSoup

url = 'https://www.saveur.com/plum-galette-recipe/'

response = get(url)
html = BeautifulSoup(response.content, 'html.parser')

recipe = {
    'title': '',
    'ingredients': [],
    'instructions': []
}

recipe['title'] = html.find('h1', class_='article_title').text

content = html.find('section', class_='content')
img_url = content.find('img', class_='image')['src']

f = open('00000001.jpg', 'wb')
f.write(get(img_url).content)
f.close()

print(recipe)
