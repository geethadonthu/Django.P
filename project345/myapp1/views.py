from django.shortcuts import render

# Create your views here.

def company(request):
    return render(request,'company.html')

def subject(request):
    return render(request,'subject.html')

def topper(request):
    return render(request,'topper.html')

