from django.urls import path
from .views import songs

urlpatterns=[
    path('songs/',songs),
]