from .forms import StudentForm
from django.http import HttpResponse
from django.shortcuts import render

def addRecord(request):
    if(request.method == "GET"):
        f1 = StudentForm()
        return render(request,"addStudent.html",{"f1":f1})
    else:
        f1=StudentForm(request.POST)
        if f1.is_valid():
            f1.save()
        return HttpResponse("record added...")    
