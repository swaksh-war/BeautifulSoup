import requests

r=requests.get('https://tracker.gg/valorant/profile/riot/UnxRon%238683/overview')

with open('valostatcontent.html','w',encoding='utf-8') as f:
    f.write(r.text)

from bs4 import BeautifulSoup

with open('valostatcontent.html',encoding='utf-8') as f:
    soup=BeautifulSoup(f,'html5lib')
match=soup.find('div',class_='table')
print(match)

