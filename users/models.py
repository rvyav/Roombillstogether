from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.urls import reverse
from sorl.thumbnail import get_thumbnail
from django.core.validators import RegexValidator
from PIL import Image
from io import BytesIO
import os, sys
from django.core.files.uploadedfile import InMemoryUploadedFile

User = settings.AUTH_USER_MODEL


class CustomUser(AbstractUser):
	GENDER_CHOICES = (
		('Male', 'Male'),
		('Woman', 'Woman'),
	)
	profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
	bio = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
	is_host = models.BooleanField(default=False)
	gender = models.CharField(max_length=30, choices=GENDER_CHOICES)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def get_absolute_url(self):
		return reverse('users:product_expense_detail', kwargs={'slug':self.slug })

	