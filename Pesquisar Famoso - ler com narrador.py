import requests
from bs4 import BeautifulSoup
import pyttsx3



pessoa = input('digite aqui o nome do famoso')
busca =f"quem e {pessoa} "
url = f"https://www.google.com/search?q={busca}"
r = requests.get(url)
s= BeautifulSoup(r.text, "html.parser")
update = s.find("div",class_="BNeawe").text
a = (busca + update)

print(a)
engine = pyttsx3.init()
engine.say(a)
engine.runAndWait()




