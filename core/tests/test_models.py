from core.models import Product, Month
from django.contrib.auth import get_user_model

import pytest
from django.urls import reverse

User = get_user_model()

pytestmark = pytest.mark.django_db


@pytest.fixture
def month():
    obj = Month.objects.create(name="january", slug="january")
    obj.save()
    yield obj

@pytest.fixture
def product():
    month = Month.objects.create(name="january", slug="january")
    month.save()
    user = User.objects.create(username="james", password="password")
    user.save()
    obj = Product.objects.create(
                            month=month,
                            user=user,
                            name="broom", 
                            slug="broom",
                            price=19.99,
                            quantity=1,
    )

    obj.save()
    
    yield obj


def test_month_model_save(month):
    assert month.name == "january"
    assert month.name == month.slug

def test_month_get_absolute_url(month, client):
    response = client.get(reverse('core:month_detail', kwargs={'slug': month.slug}))
    assert response.status_code == 200

def test_product_model_save(product):
    assert product.name == "broom"
    assert product.name == product.slug

def test_product_get_absolute_url(product, client):
    response = client.get(reverse('core:product_detail', kwargs={'slug': product.slug}))
    assert response.status_code == 200
