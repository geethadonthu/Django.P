from django.shortcuts import render

# Create your views here.
#def home(request):
    #return render(request,'home.html')


def sports(request,id):
    if id==1:
        return render(request,'app.html')
    elif id==2:
        return render(request,'app1.html')
    elif id==3:
        return render(request,'app2.html')
    

