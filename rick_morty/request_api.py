import urllib.request, json

def request_api(pm_valor, pm_model):
    for i in range (1,pm_valor):
        url_api = f'https://rickandmortyapi.com/api/character?page={i}'
        response = urllib.request.urlopen(url_api)
        libro = json.loads(response.read())

        for i in libro['results']:
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


            pm_model.objects.create(name=pm_name, status =pm_status, species=pm_species,type_r=pm_type, gender=pm_gender, origin_name=pm_origin, location_name=pm_location, image=pm_image, created=pm_created)