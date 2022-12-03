from django.shortcuts import render, redirect

from django.views.generic import View

# Create your views here.

class Index(View):
    def get(self,request):
        template_name = "rick_morty/index.html"
        return render(request, template_name)


class GenerateDB(View):
    def get(self,request):

        return redirect('index')