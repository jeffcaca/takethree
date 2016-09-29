

from __future__ import unicode_literals
from ..loginregistration.models import User
from django.db import models
import datetime
import time
import re

class Plan_Manager(models.Manager):
	def validate(self, data):
		errors = []
		bvalid = re.compile(r'^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$')

		if len(data['destination']) < 1:
			errors.append('Please enter a destination')
		if len(data['plan']) < 1:
			errors.append('Please enter a description')
		if len(data['start']) < 1:
			errors.append('Please enter a start date')
		if len(data['end']) < 1:
			errors.append('Please enter a end date')
		destinationcheck = Plan.objects.filter(destination = data['destination'])
		if destinationcheck:
			errors.append('Destination already in database!')
		if not bvalid.match(data['start']):
			errors.append('Not a valid start date')
		if not bvalid.match(data['end']):
			errors.append('Not a valid end date')
		if data['start'] > data['end']:
			errors.append('Start date can not be after end date')
		current_date = (time.strftime("%Y-%m-%d"))
		if data['start'] < current_date:
			errors.append('Start date must be in the future')
		response = {}
		if errors:
			response['passed'] = False
			response['errors'] = errors
		else:
			response['passed'] = True
		return response
	def newplanadd(self, data, user_id):
		creator = User.objects.get(id = user_id)
		createplan = Plan.objects.create(destination = data['destination'], start = data['start'], end = data['end'], plan = data['plan'], creator = creator)
		newuserplan = Plan.objects.get(id = createplan.id)
		newuserplan.userplan.add(user_id)
		newuserplan.save()
	def join(self, item_id, id):
		currentuser = User.objects.get(id = id)
		plan = Plan.objects.get(id = item_id)
 		plan.userplan.add(currentuser)
 		plan.save()

class Plan(models.Model):
	destination = models.CharField(max_length = 250)
	start = models.CharField(max_length = 100)
	end = models.CharField(max_length = 100)
	plan = models.TextField(max_length = 1000)
	creator = models.ForeignKey(User, related_name ="plancreator")
	userplan = models.ManyToManyField(User, related_name="userlink")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = Plan_Manager()