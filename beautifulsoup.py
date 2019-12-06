import requests
from bs4 import BeautifulSoup


r = requests.get('https://www.n11.com/')
source = BeautifulSoup(r.content,"lxml")
#print(source)
print(source.title)
print(r)
print(source.find("ins"))
solmenu = source.find_all("div",attrs={"class":"wrapper home"})
for link in solmenu:
   # print(link)
    print(link.find_all('a'))


