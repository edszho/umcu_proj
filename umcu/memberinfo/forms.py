from django import forms
from .models import Account, User

#Create form from database! Cool!
class AccountForm(forms.ModelForm):
	class Meta:
		model = Account
		fields = ['username', 'password']

	#override is_valid to add more checks at some point!
	def is_valid(self):
		#Basic parent check
		valid = super(AccountForm, self).is_valid()
		if not valid:
			return valid

		#Add some checks here
		#valid = check()
		return valid

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
			'firstname', 
			'middlename', 
			'lastname', 
			'gender', 
			'dob', 
			'ssn', 
			'license', 
			'license_state',
			'email',
			'occupation',
			'membership' 
		]

	def is_valid(self):
		#Basic parent check
		valid = super(UserForm, self).is_valid()

		if not valid:
			return valid

		#Add some checks here
		#valid = check()
		return valid
