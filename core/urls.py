from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'core'
urlpatterns = [
	
	path('', views.index, name='index'),
	path('home/', views.month_list, name='month_list'),
	path('create-month/', views.create_month, name='create_month'),
	path('delete-product/<slug:slug>/', views.product_delete, name='product_delete'),
	path('edit-product/<slug:slug>/', views.product_update, name='product_update'),
	path('sms-dashboard/', views.sms_dashboard, name='sms_dashboard'),
	path('create-product/', views.create_product, name='create_product'),
	path('<slug:slug>/', views.month_detail, name='month_detail'),	
	path('product/<slug:slug>/', views.product_detail, name='product_detail'),
]