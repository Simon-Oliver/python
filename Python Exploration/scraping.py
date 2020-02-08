import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



browser_options = Options()  # Options Object from the Selenium driver.
browser_options.add_argument(
    '-headless')  # No GUI More refs at : https://developer.mozilla.org/en-US/Firefox/Headless_mode#Selenium_in_python

browser = webdriver.Chrome(executable_path='./chromedriver')
# , options=browser_options
# browser = webdriver.Firefox(executable_path='geckodriver', options=browser_options)


browser.get('https://time.is')
soup = BeautifulSoup(browser.page_source, "html.parser")

num1 = soup.find(id="clock").find_all('span')

for line in num1:
    print(line.text)

