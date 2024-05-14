from django.shortcuts import render

from django.http import HttpResponse

def first(request):
    return HttpResponse("first from MyApp1")
def second(request):
    return HttpResponse("second from MyApp1")    
def welcome(request):
    uname="AFFAN KHAN"
    return render(request,"welcome.html",{"uname":uname})
def login(request):
    return render(request,"login.html",{})