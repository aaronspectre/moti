from django.urls import path
from main import views


urlpatterns = [
	path('', views.login, name = 'login'),
	path('auth', views.auth, name = 'auth'),
	path('home', views.home, name = 'home'),
	path('deliver', views.deliver, name = 'deliver'),
	path('refuse', views.refuse, name = 'refuse'),
	path('logout', views.logout, name = 'logout'),
]