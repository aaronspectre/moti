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
	if response['statusCodeValue'] == 200:
		request.session['token'] = response['body']
		return HttpResponseRedirect(reverse('home'))
	else:
		return HttpResponseRedirect(reverse('login'))


def home(request):
	if 'token' not in request.session:
		return HttpResponseRedirect(reverse('login'))

	# orders = Swagger.filter('ORDERED', request.session['token'])
	return render(request, 'home.html')


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


def categories(request):
	if 'token' not in request.session:
		return HttpResponseRedirect(reverse('login'))


	categories = Swagger.categories(request.session['token'])
	return render(request, 'panel.html', {'show_add_category': True, 'categories': categories})


def products(request):
	if 'token' not in request.session:
		return HttpResponseRedirect(reverse('login'))

	return render(request, 'panel.html', {'show_add_product': True})


def add_category(request):
	if 'token' not in request.session:
		return HttpResponseRedirect(reverse('login'))

	Swagger.createCategory(request.session['token'], (request.POST['name_uz'], request.POST['name_ru'], request.POST['name_en']))
	return HttpResponseRedirect(reverse('categories'))


def add_product(request):
	if 'token' not in request.session:
		return HttpResponseRedirect(reverse('login'))

	return HttpResponseRedirect(reverse('products'))



def logout(request):
	del request.session['token']
	return HttpResponseRedirect(reverse('login'))