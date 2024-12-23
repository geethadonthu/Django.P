from django.urls import path
from .views import reunion

urlpatterns=[
    path('reunion/',reunion),
]