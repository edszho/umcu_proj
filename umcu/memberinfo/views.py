from django.shortcuts import render
from django.http import HttpResponse
from .forms import AccountForm, UserForm

# Create your views here.

def index(request):
	return render(request, 'memberinfo/index.html', {})

def form_view(request):
	if request.method =="POST":
		form1 = AccountForm(request.POST)
		form2 = UserForm(request.POST)
		acc_form = form1
		user_form = form2	
		if form1.is_valid() and form2.is_valid():
			print "Saving"
			form1.save()
			form2.save()
			
	else:		
		acc_form = AccountForm()
		user_form = UserForm()
	return render(request, 'memberinfo/memberinfo_form.html', {'acc_form': acc_form, 'user_form': user_form})
