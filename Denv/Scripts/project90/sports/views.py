from django.shortcuts import render

# Create your views here.

def sub(request):
    return render(request,'sub.html')

def model(request):
    return render(request,'model.html')