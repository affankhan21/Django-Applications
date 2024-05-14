from django.shortcuts import render
from django.http import HttpResponse
def hello(request):
    return HttpResponse("Hello From app2")

def welcome(request):
    return HttpResponse("Welcome From app2")


