
from django.urls import path
from . import views

urlpatterns = [
   path("hello",views.hello),
   path("login",views.login),
   path("verify",views.verify),

]
