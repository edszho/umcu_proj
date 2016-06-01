from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Account(models.Model):
	username = models.CharField(max_length=20, unique=True)
	password = models.CharField(max_length=250)

class User(models.Model):
	username = models.ForeignKey(Account, on_delete=models.CASCADE)
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	middlename = models.CharField(max_length=20)
	ssn = models.CharField(max_length=9)
	dob = models.DateTimeField()
	license = models.CharField(max_length=15, null=False)
	license_state = models.CharField(max_length=12, null=False)
	occupation = models.CharField(max_length=30)
	membership = models.CharField(max_length=25)
	gender = (
			('MALE', 'Male'),
			('FEMALE', 'Female'),
			('OTHER', 'Other'),
	)
