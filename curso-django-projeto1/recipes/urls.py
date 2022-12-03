from recipes.views import *
from django.urls import path


urlpatterns = [
    path('', home), # home
    path('contato/', contato), # Contato
    path('sobre/', sobre), # Sobre
]



