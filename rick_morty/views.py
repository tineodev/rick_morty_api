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


class ListDB(View):
    def get(self, request):
        template_name = 'rick_morty/list.html'
        extra_context = {
            'lista': Pokemon.objects.all()
        }
        return render(request, template_name, extra_context)

class DetailDB(View):
    def get(self, request):
        id = 1
        template_name = 'rick_morty/detail.html'
        extra_context = {
            'personaje' : Pokemon.objects.get(id=id)
        }
        return render(request, template_name, extra_context)