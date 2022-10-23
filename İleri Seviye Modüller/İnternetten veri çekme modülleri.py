import requests

from bs4 import BeautifulSoup

url = "https://rallyinteractive.com/#spotify-fan-study"

response = requests.get(url)

html_içeriği = response.content

soup =  BeautifulSoup(html_içeriği,"https.parser")

print(soup.find_all("a"))
# her neysee
