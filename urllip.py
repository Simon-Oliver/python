import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

html = urllib.request.urlopen('https://cosylab.iiitd.edu.in/flavordb/entity_details?id=234')
soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table', {'id':'molecules'})
rows = table.find_all('tr')

flavour = []

for row in rows:
    td = row.find_all('td')
    if len(td) < 1: continue
    flavour.append(td[2].get_text())

print(len(flavour))