import json
import requests
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from main.swagger import Swagger


def login(request):
	if 'token' in request.session:
		if 'MANAGER' in request.session['roles']:
			return HttpResponseRedirect(reverse('charts'))
		return HttpResponseRedirect(reverse('home'))
	return render(request, 'login.html')


def auth(request):
	response = Swagger.auth(request.POST['username'], request.POST['password'])
	if 'token' in response:
		request.session['token'] = "Bearer " + response['token']['token']
		request.session['roles'] = response['role']
		if 'MANAGER' in response['role']:
			return HttpResponseRedirect(reverse('charts'))
		return HttpResponseRedirect(reverse('home'))
	else:
		return HttpResponseRedirect(reverse('login'))


def charts(request):
	try:
		report = Swagger.report(request.session['token'])
		most_selling = Swagger.report_most_selling(request.session['token'])
		payment_methods = Swagger.report_payment_methods(request.session['token'])
		last_30_orders = Swagger.report_last_30_orders(request.session['token'])
		return render(request, 'charts.html', {
			'report': report,
			'most_selling': most_selling,
			'payment_methods': payment_methods,
			'last_30_orders': last_30_orders
		})
	except Exception as error:
		print(error)
		return HttpResponseRedirect(reverse('logout'))


def download_report(request):
	Swagger.report_download(request.session['token'], request.POST['start'], request.POST['end'])
	with open('report.xlsx', 'rb') as report:
		data = report.read()
	response = HttpResponse(data, content_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
	response['Content-Disposition'] = 'attachment; filename=report.xlsx'
	return response


def home(request):
	try:
		if 'token' not in request.session:
			return HttpResponseRedirect(reverse('login'))

		orders = Swagger.page(request.session['token'], 0)
		return render(request, 'home.html', {'orders': orders})
	except Exception as error:
		del request.session['token']
		return HttpResponseRedirect(reverse('login'))


def update_order(request, order_id, status):
	if 'token' not in request.session:
		return HttpResponseRedirect(reverse('login'))

	Swagger.updateOrder(request.session['token'], status, order_id)
	return HttpResponse('done')


def branches(request):
	if 'token' not in request.session:
		return HttpResponseRedirect(reverse('login'))

	branches = Swagger.branches(request.session['token'])
	return render(request, 'panel.html', {'branches': branches, 'show_add_branch': True})


def add_branch(request):
	if 'token' not in request.session:
		return HttpResponseRedirect(reverse('login'))

	Swagger.createBranch(request.session['token'], request)
	return HttpResponseRedirect(reverse('branches'))


def update_branch(request, branch_id):
	if 'token' not in request.session:
		return HttpResponseRedirect(reverse('login'))

	Swagger.createBranch(request.session['token'], request, branch_id, True)
	return HttpResponseRedirect(reverse('branches'))


def delete_branch(request, branch_id):
	if 'token' not in request.session:
		return HttpResponseRedirect(reverse('login'))

	Swagger.deleteBranch(request.session['token'], branch_id)
	return HttpResponseRedirect(reverse('branches'))


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

	if 'subcategory' in request.POST:
		Swagger.createSubCategory(request.session['token'], request.POST)
	else:
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
	if 'subcategory' in request.POST:
		Swagger.createSubCategory(request.session['token'], request.POST, category_id, True)
	else:
		Swagger.createCategory(request.session['token'], data, category_id, True)
	return HttpResponseRedirect(reverse('categories'))


def subcategories(request):
	if 'token' not in request.session and 'ADMIN' not in request.session['roles']:
		return HttpResponseRedirect(reverse('login'))

	categories = Swagger.categories(request.session['token'])
	return render(request, 'panel.html', {'show_add_category': True, 'categories': categories})


def users(request):
	if 'token' not in request.session:
		return HttpResponseRedirect(reverse('login'))

	users = Swagger.users(request.session['token'])
	return render(request, 'users.html', {'users': users})


def update_user(request, user_id):
	if 'token' not in request.session:
		return HttpResponseRedirect(reverse('login'))

	Swagger.update_user(request.session['token'], request.POST, user_id)
	return HttpResponseRedirect(reverse('users'))


def change_password(request):
	if 'token' not in request.session:
		return HttpResponseRedirect(reverse('login'))

	Swagger.change_password(request.session['token'], request.POST)
	return HttpResponseRedirect(reverse('logout'))


def fees(request):
	if 'token' not in request.session:
		return HttpResponseRedirect(reverse('login'))

	fee = Swagger.fees(request.session['token'])
	return render(request, 'fee.html', {'fee': fee})


def update_fee(request):
	if 'token' not in request.session:
		return HttpResponseRedirect(reverse('login'))

	Swagger.update_fee(request.session['token'], request.POST)
	return HttpResponseRedirect(reverse('fees'))


def logout(request):
	del request.session['token']
	del request.session['roles']
	return HttpResponseRedirect(reverse('login'))