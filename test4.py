import requests


def get_photographed_obj1():
  response = requests.get('https://commons.wikimedia.org/w/api.php?action=query&prop=imagelabels&titles&format=json&titles=File:Igreja%20da%20Ordem%20Terceira%20de%20São%20Francisco%20Salvador%20Casa%20dos%20Santos%20Cristo%20Crucificado%202021-8964.jpg')
  d = response.json()
  print(d.keys())
  var = list(d.values())
  return var[1]


print(get_photographed_obj1())
