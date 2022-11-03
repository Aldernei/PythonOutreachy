from bs4 import BeautifulSoup
import requests
import re

url = 'https://www.wikidata.org/wiki/User:Aldernei_Junior/Outreachy_2'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
categoryName = soup.get_text()

params = ["Image name:","Geographic coordinates:",
          "Photographed object:", "Contributors of the page:",
          "Date and time of upload:", "Categories:"]


for i in range(6):
    result = re.search( params[i], categoryName)
    variaveisPesquisa = (result.group(0))
    print(variaveisPesquisa)
    
def get_photographed_obj1():
  url = ('https://commons.wikimedia.org/w/api.php?action=query&prop=imagelabels&titles&format=json&titles=File:Igreja%20da%20Ordem%20Terceira%20de%20São%20Francisco%20Salvador%20Casa%20dos%20Santos%20Cristo%20Crucificado%202021-8964.jpg')
  r = requests.get(url)
  r.text
  groups = re.findall(r'["]description["]:(.*)["],' ,r.text)
  return(print(groups[0]))

get_photographed_obj1()
def get_contributors1():
  url = ('https://commons.wikimedia.org/w/api.php?action=query&prop=contributors&titles&format=json&titles=File:Igreja%20da%20Ordem%20Terceira%20de%20São%20Francisco%20Salvador%20Casa%20dos%20Santos%20Cristo%20Crucificado%202021-8964.jpg')
  r = requests.get(url)
  r.text
  groups = re.findall(r'["]name["]: [.](.*)[.]' ,r.text)
  return(print(groups[0]))


get_contributors1()    
#################################################################    
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
#################################################################
