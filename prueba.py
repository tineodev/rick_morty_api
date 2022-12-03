import urllib.request, json

from datetime import datetime


url_api = f'https://rickandmortyapi.com/api/character?page=1'
response = urllib.request.urlopen(url_api)
libros = json.loads(response.read())

var_create = libros['results'][1]['created']

