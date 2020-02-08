import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

html = requests.get('https://automatetheboringstuff.com/2e/chapter0/')

# browser_options = Options()  # Options Object from the Selenium driver.
# browser_options.add_argument(
#     '-headless')  # No GUI More refs at : https://developer.mozilla.org/en-US/Firefox/Headless_mode#Selenium_in_python
#
# browser = webdriver.Chrome(executable_path='./chromedriver')
# , options=browser_options
# browser = webdriver.Firefox(executable_path='geckodriver', options=browser_options)


# browser.get('https://time.is')
soup = BeautifulSoup(html.content, "html.parser")
# browser.page_source

num1 = soup.find(class_="main")
#
# for line in num1:
#     print(line.text)

tempText = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Title of the document</title>
</head>

<body>
''' + str(num1) + '''
</body>
</html>
'''
f = open('scrapingHTML.html', "w+", encoding='utf-8')

for line in tempText:
    f.write(line)

f.close()

print('Done')