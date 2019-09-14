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
print(html.find_all('section', class_='content'))

file_name = recipe['title'].replace(' ', '_')

# f = open(file_name + '.txt', 'w+')
# f.write(str(recipe))
# f.close()

print(recipe)
