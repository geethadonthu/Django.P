from django.urls import path
from .views import sub,model

urlpatterns=[
    path('sub/',sub),
    path('model/',model),
]