from django.shortcuts import render

# Create your views here.
def function(request):
    return render(request,'function.html')

def home(request):
    return render(request,'home.html')

