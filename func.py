import requests as req
from bs4 import BeautifulSoup as bs

def parse(url, target = None):
    res = req.get(url)
    soup = bs(res.text, 'html.parser')
    themeLinks = soup.find_all('h2', class_='entry-title')

    for link in themeLinks:
        link = link.find('a')
        if link is not None:
            print(link.text + ' - ' + link.get('href'))
