import json
import requests
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.swagger import Swagger

def login(request):
	if 'token' in request.session:
		return HttpResponseRedirect(reverse('home'))
	return render(request, 'login.html')

def auth(request):
	response = Swagger.auth(request.POST['username'], request.POST['password'])
	if response['statusCode'] == 10:
		request.session['token'] = response['data']
		return HttpResponseRedirect(reverse('home'))
	else:
		return HttpResponseRedirect(reverse('login'))


def home(request):
	if 'token' not in request.session:
		return HttpResponseRedirect(reverse('login'))

	orders = Swagger.filter('ORDERED', request.session['token'])
	return render(request, 'home.html', {'orders': orders})


def deliver(request):
	if 'token' not in request.session:
		return HttpResponseRedirect(reverse('login'))

	orders = Swagger.filter('DELIVER', request.session['token'])
	return render(request, 'home.html', {'orders': orders})


def refuse(request):
	if 'token' not in request.session:
		return HttpResponseRedirect(reverse('login'))

	orders = Swagger.filter('REFUSAL', request.session['token'])
	return render(request, 'home.html', {'orders': orders})


def logout(request):
	del request.session['token']
	return HttpResponseRedirect(reverse('login'))