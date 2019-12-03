from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
import datetime
from PIL import Image
import datetime

from users.models import CustomUser


User = settings.AUTH_USER_MODEL


class Month(models.Model):
	MONTHS_CHOICES = (
		('January', 'January'),
		('February', 'February'),
		('March', 'March'),
		('April', 'April'),
		('May', 'May'),
		('June', 'June'),
		('July', 'July'),
		('August', 'August'),
		('September', 'September'),
		('October', 'October'),
		('November', 'November'),
		('December', 'December'),
	)
	name = models.CharField(max_length=50, choices=MONTHS_CHOICES)
	slug = models.SlugField(max_length=50, db_index=True, blank=True)
	created = models.DateField(default=datetime.date.today)

	class Meta:
		ordering = ('-id',)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		# save 'slug' == 'expense.name'
		self.slug = slugify(self.name)
		super(Month, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('core:month_detail', kwargs={'slug': self.slug })

	# @classmethod
	# def get_current_month_slug(cls, slug):
	# 	return cls(slug)

	# @property
	# def month_id(self):
	# 	return self.id

class Product(models.Model):
	month = models.ForeignKey(Month, on_delete=models.CASCADE, related_name='months')
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
	name = models.CharField(max_length=30)
	slug = models.SlugField(max_length=30, db_index=True, blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	quantity = models.PositiveSmallIntegerField(default=0)	
	created = models.DateTimeField(default=datetime.datetime.now())
	is_active = models.BooleanField(default=True)

	class Meta:
		ordering = ('-id',)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		# save 'slug' == 'product.name'
		self.slug = slugify(self.name)
		super(Product, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('core:product_detail', kwargs={'slug':self.slug })
