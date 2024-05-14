
from django.urls import path
from . import views

urlpatterns = [
    
    path('first',views.first),
    path("second",views.second),
    path("welcome",views.welcome),
    path("login",views.login),
]
