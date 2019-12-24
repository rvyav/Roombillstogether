from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.forms import ModelChoiceField
from django import forms
from core.models import Product, Month
from django.contrib import messages
import datetime

User = get_user_model()

class ProductForm(ModelForm):
	# Dropdown range to choose from for 'product quantity'
	PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range (1, 16)]
	# Validate forms 'quantity' as 'Integer'
	quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)

	class Meta:
		model = Product
		fields = [
				'name', 
				'price', 
				'quantity',
				'month',
	]

class MonthForm(ModelForm):
	class Meta:
		model = Month
		fields = ['name',]

	def clean(self, *args, **kwargs):
		"""
		The User cannot create a month
		that already exist.
		"""
		name = self.cleaned_data.get('name')
		if name in Month.objects.values_list('name', flat=True):
			raise forms.ValidationError(f"The month of {name} already exist")
		return super(MonthForm, self).clean(*args, **kwargs)


