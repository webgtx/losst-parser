import requests as req
from bs4 import BeautifulSoup as bs

def parse(url, target = None):
    request = req.get(url)
    soup = bs(request.text, 'html.parser')
    themeLinks = soup.find_all('h2', class_='title post-title')

    for link in themeLinks:
        link = link.find('a')
        if link is not None:
            print(link.text + ' - ' + link.get('href'))
