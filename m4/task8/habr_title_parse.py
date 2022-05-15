#Parse habr.

from bs4 import BeautifulSoup
import requests
link = "https://habr.com/ru/post/544828/"
r = requests.get(link)
soup = BeautifulSoup(r.text, 'html.parser')
for i in soup.find_all('div', class_="tm-article-presenter__header"):
    for b in i.find_all('h1', class_='tm-article-snippet__title'):
        print(b.text)
