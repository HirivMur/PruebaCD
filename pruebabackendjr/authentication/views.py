from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authtoken.views import obtain_auth_token

# Create your views here.

@csrf_exempt
def loginUser(request):
	if User.objects.filter(username='admin').count():
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				auth.login(request, user)

				return redirect('/port/')
			else:
				return redirect('/authentication/login/',status=status.HTTP_400_BAD_REQUEST)
	else:
		user = User.objects.create_user(username='admin',email='admin',password='admin')

	return render(request,'login/index.html')

def logoutUser(request):
    auth.logout(request)
    # Redirect to a success page.
    return redirect('/authentication/login/')