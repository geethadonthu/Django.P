from django.urls import path
from .views import sports
urlpatterns=[
    path("sports/<int:id>/",sports),
]