from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django import forms
from core.models import Product, Month
from core.forms import ProductForm, MonthForm
#from users.models import CustomUser
import datetime
import pytest

User = get_user_model()

pytestmark = pytest.mark.django_db

@pytest.fixture
def user():
    # Create new user
    user_ = User.objects.create(username="james")
    user_.set_password("password")
    user_.save()
    return user_

@pytest.fixture
def product_with_data(user):
    month = Month.objects.create(name="December", slug="December")
    product = Product.objects.create(
                                user=user,
                                name="broom",
                                price=19.99,
                                quantity=1,
                                month=month
    )

    data = {
        'user':product.user, 
        'name':product.name,
        'price':product.price,
        'quantity':product.quantity,
        'month':product.month.id
    }

    form = ProductForm(data=data)
    return form

@pytest.fixture
def product_with_no_data():
    month = Month.objects.create(name=" ", slug=" ")
    user = User.objects.create(username=" ", password=" ")
    product = Product.objects.create(
                                user=user,
                                name=' ',
                                price=0.0,
                                quantity=0,
                                month=month,
    )

    data = {
        'user':product.user, 
        'name':product.name,
        'price':product.price,
        'quantity':product.quantity,
        'month':product.month.id
    }

    form = ProductForm(data=data)
    return form

class TestProductForm:
    def test_product_form_with_data(self, product_with_data):
        assert True == product_with_data.is_valid()
    
    def test_product_form_with_no_data(self, product_with_no_data):
        assert False == product_with_no_data.is_valid()


class TestMonthForm:
    def test_month_forms_with_valid_data(self, user):
        month = Month.objects.create(name="December", slug="December")

        form = ProductForm(data=month)
        return form

        assert True == form.is_valid()

    def test_month_forms_with_no_valid_data(self):
        month = Month.objects.create(name=" ", slug=" ")

        form = ProductForm(data=month)
        return form

        assert False == form.is_valid()