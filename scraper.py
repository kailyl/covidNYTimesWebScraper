import requests 
from bs4 import BeautifulSoup

URL = 'https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find('title')
print(title.get_text())
paragraphs = soup.find_all('p', class_ = 'g-body')
for paragraph in paragraphs:
	print(paragraph.get_text().strip() + '\n')
