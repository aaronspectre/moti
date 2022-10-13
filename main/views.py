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
		request.session['token'] = response['body']['token']
		request.session['roles'] = response['body']['roles']
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

	orders = Swagger.filter('CANCELLED', request.session['token'])
	return render(request, 'home.html', {'orders': orders})


def categories(request):
	if 'token' not in request.session:
		return HttpResponseRedirect(reverse('login'))


	categories = Swagger.categories(request.session['token'])
	return render(request, 'panel.html', {'show_add_category': True, 'categories': categories})


def products(request):
	if 'token' not in request.session:
		return HttpResponseRedirect(reverse('login'))

	categories = Swagger.categories(request.session['token'])
	products = Swagger.products(request.session['token'])
	return render(request, 'panel.html', {'show_add_product': True, 'categories': categories, 'products': products})


def add_category(request):
	if 'token' not in request.session:
		return HttpResponseRedirect(reverse('login'))

	Swagger.createCategory(request.session['token'], (request.POST['name_uz'], request.POST['name_ru'], request.POST['name_en']))
	return HttpResponseRedirect(reverse('categories'))


def add_product(request):
	if 'token' not in request.session:
		return HttpResponseRedirect(reverse('login'))

	Swagger.createProduct(request.session['token'], request)
	return HttpResponseRedirect(reverse('products'))


def delete_product(request, product_id):
	if 'token' not in request.session:
		return HttpResponseRedirect(reverse('login'))

	Swagger.deleteProduct(request.session['token'], product_id)
	return HttpResponseRedirect(reverse('products'))


def delete_category(request, category_id):
	if 'token' not in request.session:
		return HttpResponseRedirect(reverse('login'))

	Swagger.deleteCategory(request.session['token'], category_id)
	return HttpResponseRedirect(reverse('categories'))


def update_product(request, product_id):
	if 'token' not in request.session and 'ADMIN' not in request.session['roles']:
		return HttpResponseRedirect(reverse('login'))

	Swagger.createProduct(request.session['token'], request, product_id, True)
	return HttpResponseRedirect(reverse('products'))


def update_category(request, category_id):
	if 'token' not in request.session and 'ADMIN' not in request.session['roles']:
		return HttpResponseRedirect(reverse('login'))

	data = request.POST['name_uz'], request.POST['name_ru'], request.POST['name_en']
	Swagger.createCategory(request.session['token'], data, category_id, True)
	return HttpResponseRedirect(reverse('categories'))


def update_order(request, order_id, status):
	if 'token' not in request.session:
		return HttpResponseRedirect(reverse('login'))

	Swagger.updateOrder(request.session['token'], status, order_id)
	return HttpResponseRedirect(request.META['HTTP_REFERER'])


def users(request):
	if 'token' not in request.session:
		return HttpResponseRedirect(reverse('login'))

	users = Swagger.users(request.session['token'])
	return render(request, 'users.html', {'users': users})


def update_user(request, user_id):
	if 'token' not in request.session:
		return HttpResponseRedirect(reverse('login'))

	Swagger.users(request.session['token'])
	return render(request, 'users.html', {'users': users})


def logout(request):
	del request.session['token']
	del request.session['roles']
	return HttpResponseRedirect(reverse('login'))