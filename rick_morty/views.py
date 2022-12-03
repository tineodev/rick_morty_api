from django.shortcuts import render, redirect

from django.views.generic import View

import urllib.request
import json

# Create your views here.

class Index(View):
    def get(self,request):
        template_name = "rick_morty/index.html"
        return render(request, template_name)


class GenerateDB(View):
    def get(self,request):
        url_api = 'https://rickandmortyapi.com/api/character?page=1'

        return redirect('index')