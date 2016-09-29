from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.conf.urls.static import static

def index(request):
	return render(request, 'loginregistration/index.html')

def newuser(request):
	if request.method =='POST':
		res = User.objects.register(request.POST)
	if res['created']:
		newuser = res['newuser']
		request.session['id'] = res['id']
		request.session['first_name'] = res['firstname']

		return redirect(reverse('belt:index'))
	else:
		for error in res['errors']:
			messages.error(request, error)
		return redirect(reverse('login:index'))

def login(request):
	if request.method =='POST':
		loginres = User.objects.login(request.POST)
	if loginres['created']:
		request.session['id'] = loginres['id']
		request.session['first_name'] = loginres['first_name']
		print request.session['first_name']
		return redirect(reverse('belt:index'))
	else:
		for error in loginres['errors']:
			messages.error(request, error)
		return redirect(reverse('login:index'))

def logout(request):
	request.session.clear()
	return redirect(reverse('login:index'))