import requests
import re

def get_image_name1():
  url = ('https://commons.wikimedia.org/w/api.php?action=query&prop=pageimages&titles&format=json&titles=File:Igreja%20da%20Ordem%20Terceira%20de%20São%20Francisco%20Salvador%20Casa%20dos%20Santos%20Cristo%20Crucificado%202021-8964.jpg')
  r = requests.get(url)
  r.text
  groups = re.findall(r'(File)[:](.*)( 2021-8964.jpg)' ,r.text)
  return(groups[0])

def get_geo_coordinates1():
  url = ('https://commons.wikimedia.org/w/api.php?action=query&prop=coordinates&titles&format=json&titles=File:Igreja%20da%20Ordem%20Terceira%20de%20São%20Francisco%20Salvador%20Casa%20dos%20Santos%20Cristo%20Crucificado%202021-8964.jpg')
  r = requests.get(url)
  r.text
  groups = re.findall(r'[-][0-9]{2}[.][0-9]{6}[,]' ,r.text)
  return(groups[0],groups[1])

def get_photographed_obj1():
  url = ('https://commons.wikimedia.org/w/api.php?action=query&prop=imagelabels&titles&format=json&titles=File:Igreja%20da%20Ordem%20Terceira%20de%20São%20Francisco%20Salvador%20Casa%20dos%20Santos%20Cristo%20Crucificado%202021-8964.jpg')
  r = requests.get(url)
  r.text
  groups = re.findall(r'["]description["]:(.*)["],' ,r.text)
  return(groups[0])

def get_contributors1():
  url = ('https://commons.wikimedia.org/w/api.php?action=query&prop=contributors&titles&format=json&titles=File:Igreja%20da%20Ordem%20Terceira%20de%20São%20Francisco%20Salvador%20Casa%20dos%20Santos%20Cristo%20Crucificado%202021-8964.jpg')
  r = requests.get(url)
  r.text
  groups = re.findall(r'"name":.*["]' ,r.text)
  return(groups[0])

def get_date_time1():
  url = ('https://commons.wikimedia.org/w/api.php?action=query&titles&format=json&titles=File:Igreja%20da%20Ordem%20Terceira%20de%20São%20Francisco%20Salvador%20Casa%20dos%20Santos%20Cristo%20Crucificado%202021-8964.jpg&prop=imageinfo')
  r = requests.get(url)
  r.text
  groups = re.findall(r'[0-9]{4}[-][0-9]{2}[-][0-9]{2}[T][0-9]{2}[:][0-9]{2}[:][0-9]{2}[Z]' ,r.text)
  return(groups[0])

def get_categories1():
  url = ('https://commons.wikimedia.org/w/api.php?action=query&prop=categories&titles&format=json&titles=File:Igreja%20da%20Ordem%20Terceira%20de%20São%20Francisco%20Salvador%20Casa%20dos%20Santos%20Cristo%20Crucificado%202021-8964.jpg')
  r = requests.get(url)
  r.text
  groups = re.findall(r'"Category:.*' ,r.text)
  return(groups)


print('IMAGE NAME:' , get_image_name1())
print('GEOGRAPHIC COORDINATES:', get_geo_coordinates1())
print('PHOTOGRAPHED OBJECT:' , get_photographed_obj1())
print('CONTRIBUTORS OF THE PAGE:' , get_contributors1())
print('DATE AND TIME OF UPLOAD:' , get_date_time1())
print('CATEGORIES:' , get_categories1())

print("#############################################################")
