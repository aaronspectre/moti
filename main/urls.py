from django.urls import path
from main import views


urlpatterns = [
	path('', views.login, name = 'login'),
	path('auth', views.auth, name = 'auth'),
	path('home', views.home, name = 'home'),
	path('deliver', views.deliver, name = 'deliver'),
	path('refuse', views.refuse, name = 'refuse'),
	path('products', views.products, name = 'products'),
	path('products/add', views.add_product, name = 'add_product'),
	path('categories', views.categories, name = 'categories'),
	path('categories/add', views.add_category, name = 'add_category'),
	path('logout', views.logout, name = 'logout'),
]