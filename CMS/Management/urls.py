'''from django.contrib import admin
from django.urls import path
from django.conf.urls import url
#from Management import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
		#url(r'^$', views.login, name='login'),
		url(r'register/', views.register, name='register'),
		url(r'complaint/', views.complaint, name='complaint'),
		url(r'home/', views.home, name='home'),
		url(r'logout/', views.logout, name='logout'),
		url(r'forgot/', views.forgot, name='forgot'),
		url(r'category/', views.category, name='category'),
		url(r'feedback/', views.feedback, name='feedback'),
		]
'''