from django.shortcuts import render, redirect

from django.views.generic import View, CreateView

from .models import Rick_Morty
from .request_api import request_api

from .forms import NewUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

class Index(View):
    def get(self,request):
        template_name = "rick_morty/index.html"
        return render(request, template_name)


class ListDB(View):
    def get(self, request):
        template_name = 'rick_morty/list.html'
        extra_context = {
            'lista': Rick_Morty.objects.all()
        }
        return render(request, template_name, extra_context)

class DetailDB(View):
    def get(self, request, id):
        # id = 1
        template_name = 'rick_morty/detail.html'
        extra_context = {
            'personaje' : Rick_Morty.objects.get(id=id)
        }
        return render(request, template_name, extra_context)


class MainPage(LoginRequiredMixin, View):
    def get(self, request):
        template_name = 'rick_morty/main.html'
        return render(request, template_name)

class CreateUser(CreateView):
    form_class = NewUser
    template_name = 'registration/register.html'

    def form_valid(self, form):
        form.save()
        return redirect('login')


class GenerateDB(LoginRequiredMixin, View):
    def get(self,request):
        request_api(2,Rick_Morty)
        return redirect('index')

class DeleteDB(LoginRequiredMixin, View):
    def get(self,request):
        Rick_Morty.objects.all().delete()
        return redirect('index')

