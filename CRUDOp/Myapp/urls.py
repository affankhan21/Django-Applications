

from django.urls import path
from . import views

urlpatterns = [
   
    path("hello",views.hello),
    path("addStudent",views.addStudent),
    path("showStudent",views.showAllRecords),
    path("editStudent/<sid>",views.editRecord),
    path("deleteStudent/<sid>",views.deleteRecord)



]
