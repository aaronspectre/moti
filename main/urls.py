from django.urls import path
from main import views


urlpatterns = [
	path('', views.login, name = 'login'),
	path('auth', views.auth, name = 'auth'),

	path('charts', views.charts, name = 'charts'),
	path('charts/download-report', views.download_report, name = 'download_report'),

	path('home', views.home, name = 'home'),

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
	path('users/change_password', views.change_password, name = 'change_password'),
	path('users/update/<int:user_id>', views.update_user, name = 'update_user'),

	path('fees', views.fees, name = 'fees'),
	path('fees/update', views.update_fee, name = 'update_fee'),

	path('branches', views.branches, name = 'branches'),
	path('branch/create', views.add_branch, name = 'add_branch'),
	path('branch/edit/<int:branch_id>', views.update_branch, name = 'update_branch'),
	path('branch/delete/<int:branch_id>', views.delete_branch, name = 'delete_branch'),

	path('adverts', views.adverts, name = 'adverts'),
	path('adverts/add', views.add_advert, name = 'add_advert'),
	path('adverts/delete/<int:advert_id>', views.remove_advert, name = 'remove_advert'),
	path('adverts/update/<int:advert_id>', views.update_advert, name = 'update_advert'),

	path('logout', views.logout, name = 'logout'),
]