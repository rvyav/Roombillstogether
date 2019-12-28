from django.shortcuts import (
						get_object_or_404,
						render, 
						redirect
)

from django.urls import reverse_lazy

from core.models import (
					Month, 
					Product,
)

from core.forms import (
					ProductForm,
					MonthForm,
)

from django.contrib import messages

from users.models import CustomUser

# Twilio
from django.conf import settings
from django.http import HttpResponse
from twilio.rest import Client

from .tasks import send_instant_sms

from celery import task

from django.db import transaction

import datetime


User = CustomUser

# Twilio Client
client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)


def index(request):
	pass
	return render(request, 'core/index.html')

def month_list(request):
	"""List of all the months."""
	months = Month.objects.all()

	context = {'months': months}
	return render(request, 'core/month/month-list.html', context)

@task
def month_detail(request, slug):
	"""
	Detail page of a single month.
	Also display list of expenses.
	"""
	with transaction.atomic():
		month = get_object_or_404(Month, slug=slug)

		# List of related products
		product_list = month.months.all()

		# Query 'price' field and it 'quantity'
		fields = product_list.values_list("price", "quantity")

		# Multiply 'price' field to it 'quantity'
		prices = [x * y for x, y in fields if x * y]

		# Sum of 'prices' fields
		total_price = sum(prices)

		# Price per roommate
		# round result to two decimal points
		share = round(total_price/3, 2)

		# Twilio message content
		message_broadcast = (f"'The total expense of {month} is ${total_price}.Your share to pay is ${share}.")

		# Raw query of all users names and phone numbers
		phone_numbers = dict(User.objects.filter(is_host=True).values_list("username", "phone_number"))

		# Send SMS with Celery
		if request.method == 'POST':
			for names, numbers in phone_numbers.items():
				# launch asynchronous task
				send_instant_sms.delay(message=message_broadcast)

				
		context = {
				'month': month, 
				'product_list':product_list,
				'total_price':total_price,
				'share': share
		}
		return render(request, 'core/month/month-detail.html', context)


def product_detail(request, slug):
	"""Detail page of a single product."""
	product = get_object_or_404(Product, slug=slug)

	# if the current user who purchased the item
	# equal the current user show the button in HTML
	current_user = request.user
	author = product.user

	context = {
			'product': product, 
			'author': author,
			'current_user':current_user
	}
	return render(request, 'core/product/product-detail.html', context)


def create_product(request):
	"""Create new product."""
	form = ProductForm(request.POST or None)
	# Get current month
	today = datetime.datetime.now()
	current_month = today.strftime("%B")
	if form.is_valid():
		new_form = form.save(commit=False)
		new_form.user = request.user
		# Validation the creation of a new item 
		# only for the current month
		if str(new_form.month) == current_month:
			new_form.save()
			messages.success(request, 'The product was successfully created')
			return redirect('core:month_list')
		else:
			messages.warning(request, f"Purchased can only be created for {current_month}.")

	context = {'form': form}
	return render(request, 'core/product/create-product.html', context)

def create_month(request):
	"""Create new month."""
	form = MonthForm(request.POST or None)
	if form.is_valid():
		new_form = form.save(commit=False)
		new_form.user = request.user
		new_form.save()
		messages.success(request, 'The month was successfully created')
		return redirect('core:month_list')

	context = {'form': form}
	return render(request, 'core/month/create-month.html', context)

def product_update(request, slug):
	"""Update product."""
	product = get_object_or_404(Product, slug=slug)

	form = ProductForm(request.POST or None, instance=product)
	if form.is_valid():
		form.save()
		messages.success(request, 'The product was successfully updated')
		return redirect('core:product_detail', slug=product.slug)

	context = {'form': form}
	return render(request, 'core/product/product-update.html', context)

def product_delete(request, slug):
	"""Delete product."""
	product = get_object_or_404(Product, slug=slug)

	if request.method == 'POST':
		product.delete()
		messages.success(request, 'The product has been successfully deleted')
		return redirect('core:month_list')

	context = {'product':product}
	return render(request, 'core/product/product-delete.html', context)

def sms_dashboard(request):
	pass
	return render(request, 'core/dashboard/sms_dashboard.html')


