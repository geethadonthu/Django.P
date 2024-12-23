from django.urls import path
from .views import *


app_name='myapp1'


urlpatterns=[
    path('',company, name="company"),
    path('subject/',subject,name="subject"),
    path('topper/',topper,name="topper"),

]