from __future__ import unicode_literals

from django.db import models
from localflavor.us.models import USStateField

#TODO: Think about adding "Joint" boolean. Is there a point?
class Account(models.Model):
	username = models.CharField(max_length=20, unique=True)
	password = models.CharField(max_length=250)
	def __str__(self):
		return self.username

class User(models.Model):
	username = models.ForeignKey(Account, on_delete=models.CASCADE)
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	middlename = models.CharField(max_length=20)
	ssn = models.CharField(max_length=9, unique=True)
	dob = models.DateTimeField()
	license = models.CharField(max_length=15)
	license_state = USStateField()
	occupation = models.CharField(max_length=30)
	email = models.EmailField(max_length=40, default="None")
	MEMBERSHIP_CHOICES = (
			('1', 'UM Student'), 
			('2', 'UM Grad Student'),
			('3', 'UM Hospital'),
			('4', 'UM Faculty/Staff'),
			('5', 'Alumni'),
			('6', 'Retiree'),
			('7', 'WCC'),
			('8', 'Family Member'),
			('9', 'Current Member'),
			('10', 'Other'),
		)
	membership = models.CharField(max_length=2, choices=MEMBERSHIP_CHOICES, default='1')
	GENDER_CHOICES = (
			('M', 'Male'),
			('F', 'Female'),
			('O', 'Other'),
	)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')

	is_primary = models.BooleanField(default=True)
	def __str__(self):
		return '%s %s %s' % (self.firstname, self.lastname, self.license)
