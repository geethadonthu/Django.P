from django.shortcuts import HttpResponse


def getdata(request):
    data="<h1>this is datafile</h1>"
    return HttpResponse(data)



def getmessage(request):
    data="<h1>this is getmessage to request</h1>"
    return HttpResponse(data)