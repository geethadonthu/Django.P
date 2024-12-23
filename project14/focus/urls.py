from django.urls import path
from .views import *

my_app='focus'

urlpatterns=[
    path('',sheryian, name="sheryian"),
    path('home/',home,name="home"),
    path('java/',java,name="java"),
    path('bootcamp/',bootcamp,name="bootcamp"),
    path('frontend/',frontend,name="frontend"),
    path('backend/',backend,name="backend"),
    path('apptitude/',apptitude,name="apptitude"),
    path('courses/',courses,name="courses")
]