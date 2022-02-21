from django.shortcuts import render,redirect
from django.views.generic import View
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.
class BaseView(View):
	views = {}

class HomeView(BaseView):
	def get(self,request):
		return render(request,'index.html',self.views)


@login_required
def review(request):	
	username = request.user.username
	email = request.user.email
	slug = request.POST.get('slug')
	comment = request.POST.get('comment')
	data = Review.objects.create(
		username = username,
		email = email,
		slug = slug,
		comment = comment
		)
	data.save()
	return render(request,'index.html')
	# return redirect(f"/product/{slug}")

def signup(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		cpassword = request.POST['cpassword']

		if password == cpassword:
			if User.objects.filter(username = username).exists():
				messages.error(request,'The username is already taken')
				return redirect('/signup')
			elif User.objects.filter(email = email).exists():
				messages.error(request,'The email is already taken')
				return redirect('/signup')
			else:
				user = User.objects.create_user(
					username = username,
					email = email,
					password = password
					)
				user.save()
				messages.success(request,'You are registered!')
				return render(request,'index.html')
				# return redirect('/review')

	return render(request,'signup.html')