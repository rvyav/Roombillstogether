from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
	path('', views.index, name='index'),
	path('profile/', views.profile, name='profile'),
	path('profile-expense-detail/<slug:slug>/', views.profile_expense_detail, name='profile_expense_detail'),
	path('edit-profile/<int:id>/', views.edit_profile, name='edit_profile'),
	path('register/', views.register, name='register')
]