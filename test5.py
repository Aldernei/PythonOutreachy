import requests
import re

def get_image_name1():
    
  url = ('https://commons.wikimedia.org/w/api.php?action=query&prop=pageimages&titles&format=json&titles=File:Igreja%20da%20Ordem%20Terceira%20de%20São%20Francisco%20Salvador%20Casa%20dos%20Santos%20Cristo%20Crucificado%202021-8964.jpg')
  r = requests.get(url)
  d = r.json()
  d['query']['pages']
  pageid = [id for id in d['query']['pages']]
  pageid = pageid[0]
  pageid
  return d['query']['pages'][pageid]['pageimage']
    

def get_geo_coordinates1():
  url = ('https://commons.wikimedia.org/w/api.php?action=query&prop=coordinates&titles&format=json&titles=File:Igreja%20da%20Ordem%20Terceira%20de%20São%20Francisco%20Salvador%20Casa%20dos%20Santos%20Cristo%20Crucificado%202021-8964.jpg')
  r = requests.get(url)
  d = r.json()
  d['query']['pages']
  pageid = [id for id in d['query']['pages']]
  pageid = pageid[0]
  pageid
  return d['query']['pages'][pageid]['coordinates']

def get_photographed_obj1():
  url = ('https://commons.wikimedia.org/w/api.php?action=query&prop=imagelabels&titles&format=json&titles=File:Igreja%20da%20Ordem%20Terceira%20de%20São%20Francisco%20Salvador%20Casa%20dos%20Santos%20Cristo%20Crucificado%202021-8964.jpg')
  r = requests.get(url)
  d = r.json()
  d['query']['pages']
  pageid = [id for id in d['query']['pages']]
  pageid = pageid[0]
  pageid
  return d['query']['pages'][pageid]['imagelabels']

def get_contributors1():
  url = ('https://commons.wikimedia.org/w/api.php?action=query&prop=contributors&titles&format=json&titles=File:Igreja%20da%20Ordem%20Terceira%20de%20São%20Francisco%20Salvador%20Casa%20dos%20Santos%20Cristo%20Crucificado%202021-8964.jpg')
  r = requests.get(url)
  d = r.json()
  d['query']['pages']
  pageid = [id for id in d['query']['pages']]
  pageid = pageid[0]
  pageid
  return d['query']['pages'][pageid]['contributors']

def get_date_time1():
  url = ('https://commons.wikimedia.org/w/api.php?action=query&titles&format=json&titles=File:Igreja%20da%20Ordem%20Terceira%20de%20São%20Francisco%20Salvador%20Casa%20dos%20Santos%20Cristo%20Crucificado%202021-8964.jpg&prop=imageinfo')
  r = requests.get(url)
  d = r.json()
  d['query']['pages']
  pageid = [id for id in d['query']['pages']]
  pageid = pageid[0]
  pageid
  var = d['query']['pages'][pageid]['imageinfo']
  listToStr = ' '.join(map(str, var))
  listToStr
  groups = re.findall(r'[{](.*)[,]', listToStr)
  return groups


def get_categories1():
  url = ('https://commons.wikimedia.org/w/api.php?action=query&prop=categories&titles&format=json&titles=File:Igreja%20da%20Ordem%20Terceira%20de%20São%20Francisco%20Salvador%20Casa%20dos%20Santos%20Cristo%20Crucificado%202021-8964.jpg')
  r = requests.get(url)
  d = r.json()
  d['query']['pages']
  pageid = [id for id in d['query']['pages']]
  pageid = pageid[0]
  pageid
  return d['query']['pages'][pageid]['categories']



print('IMAGE NAME:' , get_image_name1())
print('GEOGRAPHIC COORDINATES:', get_geo_coordinates1())
print('PHOTOGRAPHED OBJECT:' , get_photographed_obj1())
print('CONTRIBUTORS OF THE PAGE:' , get_contributors1())
print('DATE AND TIME OF UPLOAD:' , get_date_time1())
print('CATEGORIES:' , get_categories1())

print("#############################################################")
