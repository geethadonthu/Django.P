from django.urls import path
from .views import home,service

urlpatterns=[
    path('home/',home),
    path('service/', service),
]