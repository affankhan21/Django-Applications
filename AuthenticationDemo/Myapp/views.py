from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.forms import authenticate

def profile(request):
    return render(request,"Myapp/profile.html",{})
def register(request):
    if request.method=="GET":
        form=UserCreationForm()
        return render(request,"registrattion/register.html",{"form":form})
    else:
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("Error")
        return redirect("/")        



