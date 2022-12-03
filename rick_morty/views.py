from django.shortcuts import render, redirect

from django.views.generic import View

from .models import Pokemon
from .request_api import request_api
import urllib.request, json


# Create your views here.

class Index(View):
    def get(self,request):
        template_name = "rick_morty/index.html"
        return render(request, template_name)


class GenerateDB(View):
    def get(self,request):
        request_api(2,Pokemon)
        return redirect('index')

class DeleteDB(View):
    def get(self,request):
        Pokemon.objects.all().delete()
        return redirect('index')