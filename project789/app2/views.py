from django.shortcuts import render

# Create your views here.

def travel(request):
    return render(request,'travel.html')

def trip(request):
    return render(request,'trip.html')

def rest(request):
    return render(request,'rest.html')
