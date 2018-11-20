import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#res = requests.get('https://www.wikipedia.org')
#print(res.text)
my_url = 'https://www.wikipedia.org'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
print(page_soup.h1)
print(page_soup.p)
#soup = bs4.BeautifulSoup(res.text, 'lxml')
#title = soup.select('title')
#print(title[0].getText())
# Create csv file from content
