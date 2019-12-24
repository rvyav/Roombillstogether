from core.models import Product, Month
from django.contrib.auth import get_user_model

import pytest
from django.urls import reverse

User = get_user_model()

pytestmark = pytest.mark.django_db


@pytest.fixture
def month():
    month_ = Month.objects.create(name="january", slug="january")
    return month_

@pytest.fixture
def product():
    month = Month.objects.create(name="january", slug="january")
    user = User.objects.create(username="james", password="password")
    product = Product.objects.create(
                            month=month,
                            user=user,
                            name="broom", 
                            slug="broom",
                            price=19.99,
                            quantity=1,
    )
    return product

class TestMonthModel:
    def test_month_model_save(self, month):
        assert month.name == "january"
        assert month.name == month.slug

    def test_month_get_absolute_url(self, month, client):
        response = client.get(reverse('core:month_detail', kwargs={'slug': month.slug}))
        assert response.status_code == 200

    def test_product_model_save(self, product):
        assert product.name == "broom"
        assert product.name == product.slug

    def test_product_get_absolute_url(self, product, client):
        response = client.get(reverse('core:product_detail', kwargs={'slug': product.slug}))
        assert response.status_code == 200
