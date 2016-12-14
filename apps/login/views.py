from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from . import models
from .models import User

def index(request):
	if not 'first_name' in request.session:
		request.session['first_name'] = ""

	return render(request, "login/index.html")

def success(request):

	first_name = request.session['first_name']

	return render(request, "login/success.html",)

def register_process(request):
	errors =[]
	if request.method == "POST":
		result = User.userMgr.register(request.POST['first_name'],request.POST['last_name'],request.POST['email'],request.POST['password'], request.POST['confirm_password'])

		if result[0]==True:
			request.session['first_name'] = result[1].first_name
			print result, "*******************************************************"
			# request.session.pop('errors')
			return redirect('/success')
		else:
			request.session['errors'] = result[1]
			return redirect('/')
	else:

		return redirect ('/')

def login_process(request):

	errors =[]
	result = User.userMgr.login(request.POST['email'],request.POST['password'])
	print result, "**************************************************************"

	if result[0] == True:
		request.session['first_name'] = result[1][0].first_name
		# We have result[1][0] this refers to the results of the query (user query returned) and index of zero which is what we just unwrapped.
		print request.session['first_name'], "**************************************************************"
		return redirect('/success')

	else:
		request.session['errors'] = result[1]
		return redirect('/')
