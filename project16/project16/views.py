from django.shortcuts import render

def home(request):
    data='python'
    data1='django'
    return render(request,'home.html',context={'data':data,'data1':data1})