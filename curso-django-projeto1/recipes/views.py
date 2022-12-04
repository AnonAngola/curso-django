from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name':'Kahilo pedro Massango - Inserido usando context '
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html')
