import urllib
from bs4 import BeautifulSoup
import requests
import webbrowser

text = 'where is London'

text = urllib.parse.quote_plus(text)

url = 'https://www.google.com/search?q='+ text
print(url)

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

country = soup.find('h3', class_ = 'r').a.text
print(country)