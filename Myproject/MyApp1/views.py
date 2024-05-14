from django.shortcuts import render
from django.http import HttpResponse
def hello(request):
    return HttpResponse("Hello From app1")

# Create your views here.
