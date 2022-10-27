from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views

from .views import ExampleView

urlpatterns = [
    path('', ExampleView.as_view()),
    path('login/', views.obtain_auth_token)
]