from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.index, name="index"),
	url(r"travels/add", views.addtravelplan, name="addplan"),
	url(r"travels/newplan", views.newplan, name="newplan"),
	url(r"travels/join/(?P<id>\d+)$", views.joinin, name="join"),
	url(r"travels/destinations/(?P<id>\d+)$", views.viewplans, name="viewplan"),
	
	
]

	