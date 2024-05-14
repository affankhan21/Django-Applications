
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("first/",include("Myapp1.urls")),
     path("second/",include("Myapp2.urls")),
]
