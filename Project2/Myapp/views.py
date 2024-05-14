from django.shortcuts import render,redirect
from django.http import HttpResponse

def hello(request):
    return HttpResponse("hello from myapp")
def login(request):
    return render(request,"login.html",{})
def verify(request):
    uname=request.POST["uname"]
    pwd=request.POST["pwd"]
    if uname=="Affan" and pwd=="Affan@21":
       return render(request,"welcome.html",{"uname":uname})
    else:
        return redirect(login)

        