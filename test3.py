from bs4 import BeautifulSoup
import requests
import re

#Acess the webpage that contains parameters names and the API calls
url = 'https://www.wikidata.org/wiki/User:Aldernei_Junior/Outreachy_2'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
soup.prettify()

#Getting the parameters from the page 
params = []
for nome in soup.find_all("div", attrs={"class":"param"}):
    nomes_params = []
    nomes_params.append(nome.get('id'))
    params.append(nomes_params)

#Getting the API URLs from the page 
api_calls = []
for link in soup.find_all("a", attrs={"class":"external free"}):
    dados_chamadas = []
    dados_chamadas.append(link.get('href'))
    api_calls.append(dados_chamadas)

#Loop used for joining and printing the parameters and their respective URL calls


i = 0
x = 0
y = 0
while i < 10:
    while y < len(api_calls):
        print(params[x] + api_calls[y])
        x += 1
        y += 1
        if x == 6:
            x = 0

i += 1
