import requests

def get_params_data(filename,param):
  if (param == 'title'):
    url = ('https://commons.wikimedia.org/w/api.php?action=query&prop=pageimages&titles&format=json&titles='+filename)
    x = ('pageimage')
  elif (param == 'coordinates'):
    url = ('https://commons.wikimedia.org/w/api.php?action=query&prop=coordinates&titles&format=json&titles='+filename)
    x = ('coordinates')
  elif (param == 'AIdescription'):
    url = ('https://commons.wikimedia.org/w/api.php?action=query&prop=imagelabels&titles&format=json&titles='+filename)
    x = ('imagelabels')
  elif (param == 'contributors'):
    url = ('https://commons.wikimedia.org/w/api.php?action=query&prop=contributors&titles&format=json&titles='+filename)
    x = ('contributors')
  elif (param == 'uploaddata'):
    url = ('https://commons.wikimedia.org/w/api.php?action=query&titles&format=json&titles='+filename+'&prop=imageinfo')
    x = ('imageinfo')
  elif (param == 'categories'):
    url = ('https://commons.wikimedia.org/w/api.php?action=query&prop=categories&titles&format=json&titles='+filename)
    x = ('categories')
  else:
    print("invalid parameter or parameter doesn't exist")
  r = requests.get(url)
  d = r.json()
  d['query']['pages']
  pageid = [id for id in d['query']['pages']]
  pageid = pageid[0]
  pageid
  return d['query']['pages'][pageid][x]

print(get_params_data('File:Forte Príncipe da Beira.jpg',
                      'categories'))
