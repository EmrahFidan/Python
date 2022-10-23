import requests
from bs4 import BeautifulSoup

url = "https://www.doviz.com/"
respone = requests.get(url)
doviz = respone.content
icerik = BeautifulSoup(doviz,"html.parser")

name = icerik.find_all("span",{"class":"name"})
value = icerik.find_all("span",{"class":"value"})

for n,v in zip(name,value):
    print("{} = {} ".format(n.text,v.text))