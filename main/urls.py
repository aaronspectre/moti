from django.urls import path
from main import views


urlpatterns = [
	path('', views.login, name = 'login'),
	path('auth', views.auth, name = 'auth'),

	path('home', views.home, name = 'home'),
	path('home/filter', views.filter, name = 'filter'),

	path('home/order', views.create_order, name = 'create_order'),
	path('update/<int:order_id>/<str:status>', views.update_order, name = 'update_order'),

	path('products', views.products, name = 'products'),
	path('products/add', views.add_product, name = 'add_product'),
	path('products/update/<int:product_id>', views.update_product, name = 'update_product'),
	path('products/delete/<int:product_id>', views.delete_product, name = 'delete_product'),

	path('categories', views.categories, name = 'categories'),
	path('categories/add', views.add_category, name = 'add_category'),
	path('categories/update/<int:category_id>', views.update_category, name = 'update_category'),
	path('categories/delete/<int:category_id>', views.delete_category, name = 'delete_category'),

	path('users', views.users, name = 'users'),
	path('users/update/<int:user_id>', views.update_user, name = 'update_user'),

	path('fees', views.fees, name = 'fees'),
	path('fees/add', views.add_fee, name = 'add_fee'),
	path('fees/update/<int:fee_id>', views.update_fee, name = 'update_fee'),

	path('branches', views.branches, name = 'branches'),
	path('branch/create', views.add_branch, name = 'add_branch'),
	path('branch/edit/<int:branch_id>', views.update_branch, name = 'update_branch'),
	path('branch/delete/<int:branch_id>', views.delete_branch, name = 'delete_branch'),

	path('logout', views.logout, name = 'logout'),
]