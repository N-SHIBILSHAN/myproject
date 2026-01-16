from django.shortcuts import render
from django.http import HttpResponse

def page1(request):
    return HttpResponse("hello world!")

def page2(request):
    return HttpResponse("shibil")
def page(request):
    return render(request,'myfile.html')
def page3(request):
    return render(request,'login.html')