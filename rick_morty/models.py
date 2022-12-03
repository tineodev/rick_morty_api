from django.db import models

# Create your models here.

class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    species = models.CharField(max_length=20)
    type_r = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    origin_name = models.CharField(max_length=100)
    location_name = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    episode = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=False, auto_now_add=False)

    class Meta:
        db_table = 'db_characters'


