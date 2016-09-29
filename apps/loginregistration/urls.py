from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^newuser$", views.newuser, name="newuser"),
 	url(r"^login$", views.login, name="log"),
 	url(r"^logout$", views.logout, name="logout")

 
]