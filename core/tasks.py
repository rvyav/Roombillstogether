from django.contrib.auth import get_user_model

from celery import task
from core.models import Month, Product

# Twilio
from django.conf import settings
from django.http import HttpResponse
from twilio.rest import Client

User = get_user_model()

# Twilio Client
client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)

# Twilio message content
message_broadcast = (f"'The total expense of X is $Y.Your share to pay is $Z.")

# Raw query of all users names and phone numbers
phone_numbers = dict(User.objects.filter(is_host=True).values_list("username", "phone_number"))

@task
def send_instant_sms(*args, **kwargs):
    for names, numbers in phone_numbers.items():
        message = client.messages.create(from_ = settings.PHONE_NUMBER,
										body = message_broadcast, 
										to = numbers)
