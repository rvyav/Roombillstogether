from django.contrib.auth import get_user_model

from celery import task
from core.models import Month, Product
from users.models import CustomUser
import pytest

# Twilio
from django.conf import settings
from django.http import HttpResponse
from twilio.rest import Client

from core.models import Product

User = get_user_model()

pytestmark = pytest.mark.django_db

@pytest.fixture
def valid_users():
    # Create new users
    User.objects.create(
                        username="james007",
                        first_name="james",
                        last_name="bond",
                        is_host=True,
                        phone_number="9179998080",
    )
    User.objects.create(
                        username="hannah1890",
                        first_name="hannah",
                        last_name="williams",
                        is_host=False,
                        phone_number="2123456778",
    )
    User.objects.create(
                        username="ronaldo11",
                        first_name="ronald",
                        last_name="dowty",
                        is_host=True,
                        phone_number="2334248800",
    )
    user_list = User.objects.all()
    return user_list

@pytest.fixture
def invalid_users():
    # create new users
    User.objects.create(
                        username="charlene2k",
                        first_name="charlene",
                        last_name="duvalle",
                        is_host=True,
                        phone_number="",
    )
    User.objects.create(
                        username="will_the_kid",
                        first_name="william",
                        last_name="dutch",
                        is_host=False,
                        phone_number="9907781234",
    )
    user_list = User.objects.all()
    return user_list

class TestUsers:
    def test_list_valid_hosts_and_their_phone_numbers(self, valid_users):
        all_users_and_phone_numbers = dict(User.objects.filter(is_host=True).values_list("username", "phone_number"))
        number_of_users = User.objects.count()

        assert all_users_and_phone_numbers['james007'] == '9179998080'
        assert number_of_users == 3

    def test_valid_user_missing_phone_number(self, invalid_users):
        users_and_phone_numbers = dict(User.objects.filter(is_host=True).values_list("username", "phone_number"))

        assert users_and_phone_numbers['charlene2k'] == ''

    def test_user_is_not_host(self, invalid_users):
        active_users_and_phone_numbers = User.objects.filter(is_host=False).count()
        number_of_users = User.objects.count()

        assert active_users_and_phone_numbers == 1
        assert number_of_users == 2

class TestSendSMS:
    pass
