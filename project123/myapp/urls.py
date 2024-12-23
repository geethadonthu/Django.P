from django.urls import path
from .views import home,sports,movies

app_name='myapp'


urlpatterns=[
    path('',home, name="home"),
    path('sports/',sports, name="sports"),
    path('movies/',movies, name="movies"),
]