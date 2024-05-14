from django.shortcuts import render,redirect
from django.http import  HttpResponse
from Myapp.models import Student
def hello(request):
    return HttpResponse("I AM HELLO FROM MYAPP")
def addStudent(request):
    if request.method=="GET":
      return render(request,"addStudent.html",{})   
    else:
        sname=request.POST["sname"]   
        age=request.POST["age"]   
        percentage=request.POST["percentage"]
        location=request.POST["location"]
        s1=Student(sname=sname,age=age,percentage=percentage,location=location)
        s1.save()
        return redirect(showAllRecords)
def showAllRecords(request):
    student=Student.objects.all()
    return render(request,"showAllRecords.html",{"student":student}) 

def editRecord(request,sid):
    s1=Student.objects.get(id=sid)
    if request.method=="GET":
        return render(request,"editConfirm.html",{"student":s1})
    else:
        sname=request.POST["sname"]   
        age=request.POST["age"]   
        percentage=request.POST["percentage"]
        location=request.POST["location"]
        s1.sname=sname
        s1.age=age
        s1.percentage=percentage
        s1.location=location
        s1.save()
        return redirect(showAllRecords)

def deleteRecord(request,sid):
    if request.method=="GET":
        return render(request,"deleteConfirm.html",{})
    else:    
       action=request.POST["action"]
       if action=="yes":
            s1=Student.objects.get(id=sid)
            s1.delete()
    return redirect(showAllRecords)