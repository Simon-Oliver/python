from requests import get
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/search/title/?release_date=2017&sort=num_votes,desc&page=1'


def scrape_movies(link):
    obj = []

    response = get(link)

    html_soup = BeautifulSoup(response.text, 'html.parser')
    movie_containers = html_soup.find_all(
        'div', class_='lister-item mode-advanced')

    for container in movie_containers:
        obj.append(container.h3.a.text)

    return obj


data = scrape_movies(url)
print(data)
