from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

geckodriver = '/Users/Simon/Desktop/Coding/python/geckodriver'
url = "https://www.saveur.com/vietnamese-daikon-carrot-pickles-recipe/"

options = webdriver.FirefoxOptions()
options.add_argument('-headless')

browser = webdriver.Firefox(executable_path=geckodriver, firefox_options=options)
browser.get(url)
ele = browser.find_element_by_class_name('element-rawhtml')
print(ele)

# content = browser.page_source

browser.quit()

# html = BeautifulSoup(content, 'html.parser')

# recipe = {
#     'title': '',
#     'ingredients': [],
#     'instructions': []
# }
#
# recipe['title'] = html.find('h1', class_='article_title').text
# print(html.find_all('section', class_='content'))

# file_name = recipe['title'].replace(' ', '_')

# f = open(file_name + '.txt', 'w+')
# f.write(str(recipe))
# f.close()

# print(recipe)
