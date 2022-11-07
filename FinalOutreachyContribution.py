import requests

def get_image_name(filename):
    
  url = ('https://commons.wikimedia.org/w/api.php?action=query&prop=pageimages&titles&format=json&titles='+filename)
  r = requests.get(url)
  d = r.json()

  pageid = [id for id in d['query']['pages']]
  pageid = pageid[0]
  pageid
  return d['query']['pages'][pageid]['title']
    

def get_geo_coordinates(filename):
  url = ('https://commons.wikimedia.org/w/api.php?action=query&prop=coordinates&titles&format=json&titles='+filename)
  r = requests.get(url)
  d = r.json()

  pageid = [id for id in d['query']['pages']]
  pageid = pageid[0]
  pageid
  coordinates_item = d['query']['pages'][pageid]['coordinates']
  
  lat = []
  lon = []
  for item in coordinates_item:
   lat.append(item['lat'])
   lon.append(item['lon'])
  return (lat, lon)

def get_AI_description(filename):
  url = ('https://commons.wikimedia.org/w/api.php?action=query&prop=imagelabels&titles&format=json&titles='+filename)
  r = requests.get(url)
  d = r.json()

  pageid = [id for id in d['query']['pages']]
  pageid = pageid[0]
  pageid

  try:
    descriptions_item = d['query']['pages'][pageid]['imagelabels']

    dscr = []
    for item in descriptions_item:
     dscr.append(item['description'])
    return dscr

  except KeyError:
   return "Talvez a chave não exista para este arquivo, confira o arquivo JSON."

def get_contributors(filename):
  url = ('https://commons.wikimedia.org/w/api.php?action=query&prop=contributors&titles&format=json&titles='+filename)
  r = requests.get(url)
  d = r.json()
  
  pageid = [id for id in d['query']['pages']]
  pageid = pageid[0]
  pageid

  contributors_item = d['query']['pages'][pageid]['contributors']

  var = []
  for item in contributors_item:
   var.append(item['name'])
  return var


def get_date_time(filename):
  url = ('https://commons.wikimedia.org/w/api.php?action=query&titles&format=json&titles='+filename+'&prop=imageinfo')
  r = requests.get(url)
  d = r.json()

  pageid = [id for id in d['query']['pages']]
  pageid = pageid[0]
  pageid
  dates_item = d['query']['pages'][pageid]['imageinfo']

  date = []
  for item in dates_item:
    date.append(item['timestamp'])
  return date


def get_categories(filename):
  url = ('https://commons.wikimedia.org/w/api.php?action=query&prop=categories&titles&format=json&titles='+filename)
  r = requests.get(url)
  d = r.json()

  pageid = [id for id in d['query']['pages']]
  pageid = pageid[0]
  pageid
  categories_item = d['query']['pages'][pageid]['categories']

  category = []
  for item in categories_item:
   category.append(item['title'])
  return category

#exemplo de requisição:
print(get_date_time("File:Igreja da Ordem Terceira de São Francisco Salvador Casa dos Santos Cristo Crucificado 2021-8964.jpg"))
