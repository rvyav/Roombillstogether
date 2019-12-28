from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django import forms
from core.models import Product, Month
from core.forms import ProductForm, MonthForm
from users.models import CustomUser
from django.urls import reverse
from django.test import Client

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
def product(user):
    # Create new product
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
        'month':product.month.name
    }

    form = ProductForm(data=data)
    return form

@pytest.fixture
def month(user):
    # Create new month
    month = Month.objects.create(name="December", slug="December")
    form = ProductForm(data=month)
    return form

@pytest.fixture
def logged_in():
    # Log in the user
    client = Client()
    user_is_logged_in = client.login(username='james', password='password')
    return user_is_logged_in

@pytest.fixture
def current_month():
    # Return the current month
    today = datetime.datetime.now()
    current_month_ = today.strftime("%B")
    return current_month_


class TestProduct:
    def test_product_list(self, user):
        month = Month.objects.create(name="january", slug="january")
        Product.objects.create(
                            month=month,
                            user=user,
                            name="broom", 
                            slug="broom",
                            price=19.99,
                            quantity=2,
        )
        Product.objects.create(
                            month=month,
                            user=user,
                            name="table", 
                            slug="table",
                            price=99.99,
                            quantity=1,
        )

        product_list = Product.objects.filter(is_active=True)

        assert product_list is not None
        assert len(product_list) == 2

    def test_product_detail(self, client, user):
        month = Month.objects.create(name="january", slug="january")
        product = Product.objects.create(
                                month=month,
                                user=user,
                                name="Tv stand", 
                                slug="Tv stand",
                                price=39.99,
                                quantity=1,
        )
        
        assert product is not None


    def test_create_product(self, product, logged_in, current_month):
        assert logged_in == True
        assert product.data['month'] == current_month
        assert str(product.data['user']) == 'james'
        

    def product_delete(self):
        pass

class TestMonth:
    def test_month_list(self):
        Month.objects.create(name="january", slug="january")
        Month.objects.create(name="february", slug="february")
        Month.objects.create(name="mars", slug="mars")
        
        months_list = Month.objects.all()
        
        assert months_list is not None
        assert len(months_list) == 3

    def test_month_detail(self):
        pass

    def test_create_month(self, month, logged_in, current_month):
        assert logged_in == True
        assert month.data.name == current_month

        