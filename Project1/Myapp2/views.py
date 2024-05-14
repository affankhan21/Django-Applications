from django.shortcuts import render

from django.http import HttpResponse

def first(request):
    return HttpResponse("first from MyApp2")
def second(request):
    return HttpResponse("second from MyApp2")    

