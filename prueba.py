import urllib.request, json

from datetime import datetime


url_api = f'https://rickandmortyapi.com/api/character?page=1'
response = urllib.request.urlopen(url_api)
libros = json.loads(response.read())

for i in libros['results']:
    pm_id =i['id']
    pm_name =i['name']
    pm_status = i['status']
    pm_species =i['species']
    pm_type =i['type']
    pm_gender =i['gender']
    pm_origin =i['origin']['name']
    pm_location =i['location']['name']
    pm_image =i['image']
    #! pm_episode =i['episode']
    pm_created =i['created']

    print(pm_name)
    print(pm_status)
    print(pm_species)
    print(pm_type)
    print(pm_gender)
    print(pm_origin)
    print(pm_location)
    print(pm_image)
    print(pm_created)

    Pokemon.object.create(name=pm_name, status =pm_status, species=pm_species,type_r=pm_type, gender=pm_gender, origin_name=pm_origin, location_name=pm_location, image=pm_image, created=pm_created)


