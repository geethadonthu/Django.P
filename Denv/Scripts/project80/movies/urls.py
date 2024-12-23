from django.urls import path
from .views import function,home

urlpatterns=[
    path('function/',function),
    path('home/',home),
]