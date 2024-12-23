from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')


def sports(request):
    return render(request,'sports.html')

def movies(request):
    return render(request,'movies.html')
