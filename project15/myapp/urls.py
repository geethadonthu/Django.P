from django.urls import path
from .views import *

app_name='myapp'

urlpatterns=[
    path('',sheryians,name='sheryians'),
    path('home/',home,name='home'),
    path('java/',java,name='java'),
    path('frontend/',frontend,name='frontend'),
    path('backend/',backend,name='backend'),
    path('bootcamp/',bootcamp,name='bootcamp'),
    path('aptitude/',aptitude,name='aptitude'),
    path('courses/',courses,name='courses')
]