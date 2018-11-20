import requests
import bs4

res = requests.get('https://www.wikipedia.org')
#print(res.text)

soup = bs4.BeautifulSoup(res.text, 'lxml')
title = soup.select('title')
print(title[0].getText())
