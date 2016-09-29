from django.shortcuts import render, HttpResponse, redirect
from ..loginregistration.models import User
from .models import Plan
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.conf.urls.static import static


def index(request):
	context = {
	'myplans': Plan.objects.filter(userplan = request.session['id']),
	'othersplans': Plan.objects.exclude(userplan = request.session['id'])
	}
	return render(request, 'belt/index.html', context)

def addtravelplan(request):
	return render(request, 'belt/addtravel.html')
def viewplans(request, id):
	plan = Plan.objects.get(id = id)
	users = User.objects.filter(userlink = plan)
	context = {
	'plan': plan,
	'users': users
	}
	return render(request, 'belt/viewplan.html', context)

def newplan(request):
	if request.method == "POST":
		result = Plan.objects.validate(request.POST)
	if result['passed']:
		newplan = Plan.objects.newplanadd(request.POST, request.session['id'])
		return redirect(reverse('belt:index'))
	else:
		for error in result['errors']:
			messages.error(request, error)
		return redirect(reverse('belt:addplan'))
def joinin(request, id):
 	if request.method == "POST":
 		plan = Plan.objects.get(id = id)
 		join = Plan.objects.join(plan.id, request.session['id'])
 	return redirect(reverse('belt:index'))
