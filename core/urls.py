from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views

from .views import ExampleView, CadPerguntas, GetPerguntas

urlpatterns = [
    path('', ExampleView.as_view()),
    path('login/', views.obtain_auth_token),
    path('cad_perguntas', CadPerguntas.as_view()),
    path('get_perguntas', GetPerguntas.as_view()),
]