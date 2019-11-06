from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.forms import ModelChoiceField
from django import forms
from core.models import Product, Month
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

	def clean(self, *args, **kwargs):
		"""
		The User can only 
		choose the current month.
		"""
		# Get current month
		today = datetime.datetime.now()
		current_month = today.strftime("%B")
		# Compare to month in forms
		month = self.cleaned_data.get('month')
		if str(month) == current_month:
			return super(ProductForm, self).clean(*args, **kwargs)
		else:
			raise forms.ValidationError(f"Purchased can only be created for {current_month}.")

class MonthForm(ModelForm):
	class Meta:
		model = Month
		fields = ['name',]

