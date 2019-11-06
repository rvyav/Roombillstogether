from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django import forms
from core.models import Product, Month
from core.forms import ProductForm, MonthForm
import datetime
import pytest

User = get_user_model()

pytestmark = pytest.mark.django_db


class TestProductForm:
    def test_product_forms_with_valid_data(self):
        month = Month.objects.create(name="january", slug="january")
        month.save()
        user = User.objects.create(username="james", password="password")
        obj = Product.objects.create(
                                user=user,
                                name="broom",
                                price=19.99,
                                quantity=1,
                                month=month,
        )
        
        form = ProductForm(data=obj)
        return form
        assert True == form.is_valid()

    def test_product_forms_with_no_valid_data(self):
        month = Month.objects.create(name="january", slug="january")
        month.save()
        user = User.objects.create(username="james", password="password")
        obj = Product.objects.create(
                                user=user,
                                name=" ",
                                price=0.00,
                                quantity=10,
                                month=month,
        )
        
        form = ProductForm(data=obj)
        return form
        assert False == form.is_valid()


class TestMonthForm:
    def test_month_forms_with_valid_data(self):
        month = Month.objects.create(name="january", slug="january")
        month.save()
        user = User.objects.create(username="james", password="password")
        
        form = ProductForm(data=month)
        return form
        assert True == form.is_valid()

    def test_month_forms_with_no_valid_data(self):
        month = Month.objects.create(name=" ", slug=" ")
        month.save()
        user = User.objects.create(username="james", password="password")

        form = ProductForm(data=month)
        return form
        assert False == form.is_valid()
    
# pytestmark = pytest.mark.django_db

# @pytest.fixture
# def product_form():
#     month = Month.objects.create(name="january", slug="january")
#     #month.save()
#     user = User.objects.create(username="james", password="password")
#     obj = Product.objects.create(
#                                 user=user,
#                                 name="broom",
#                                 price=19.99,
#                                 quantity=1,
#                                 month=month,
#     )
#     # obj.save()
        
#     form = ProductForm(data=obj)
#     return form
#     yield form

# def test_forms_with_valid_data(product_form):
#     assert True == form.is_valid()

# def test_forms_with_no_data(product_form):
#     form_data = {
#             'month': '',
#             'user': '',
#             'name': '',
#             'slug': '',
#             'price': '',
#             'quantity':'',
#         }

#     form = ProductForm(data=form_data)
#     assert form.is_valid()
    
