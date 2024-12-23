from django.urls import path
from .views import *

app_name='app2'

urlpatterns=[
    path('',travel,name="travel"),
    path('trip',trip,name="trip"),
    path('rest',rest,name="rest"),
]