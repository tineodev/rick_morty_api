import urllib.request, json

def request_api(pm_valor):
    for i in range (1,pm_valor):
        url_api = f'https://rickandmortyapi.com/api/character?page={pm_valor}'
        response = urllib.request.urlopen(url_api)
        libros = json.loads(response.read())
