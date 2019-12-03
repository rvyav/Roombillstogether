# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from django.forms import ModelForm
# from django import forms
# from users.models import CustomUser
# from users.forms import UserRegistrationForm
# import datetime
# import pytest

# from django.contrib.auth.forms import UserCreationForm

# User = get_user_model()

# pytestmark = pytest.mark.django_db

# # class UserTestCase(TestCase):
# #     def test_registration_form(self):
# #         user = User.objects.create(username="james", password="password")


# #         data = {
# #             'username':"james",
# #             'password':"password",
# #         }

# #         form = UserRegistrationForm(data=data)
# #         self.assertTrue(form.is_valid())
    

#     # def test_registration_form(self):
#     #     user = User.objects.create(username="james", password="password")


#     #     data = {
#     #         'username':"james",
#     #         'password':"password",
#     #     }

#     #     form = UserRegistrationForm(data=data)
#     #     self.assertTrue(form.data["username"])


#     # def test_form_return_right_data(self):
#     #     user = User.objects.create(username="james", password="password")

#     #     data = {
#     #         'username':"james",
#     #         'password':"password",
#     #     }

#     #     form = UserRegistrationForm(data=data)
#     #     self.assertTrue(form.data["username"])

# @pytest.fixture
# def users():
#     user = User.objects.create(id=1)

#     #obj = CustomUser.objects.get(id=1)

#     data = {
#         #'id':user_id, 
#         'username':user_id, 
#         'first_name':user.first_name,
#         'last_name':user.last_name,
#         'email':user.email,
#         'password':user.password,
#         #'password2':user.password2,
#     }

#     form = UserRegistrationForm(data=data)
#     yield form

# def test_user_creation_form_with_data(users):
#     assert True is not None
#     assert True == users.is_valid()
#     #assert users.data["id"] == 1

# # def test_user_form_return_right_data(users):
# #     assert users.data["username"] == "james"
# #     assert users.data["password"] == "password"

# # class TestProductForm:
# #     def test_product_forms_with_valid_data(self):
# #         month = Month.objects.create(name="january", slug="january")
# #         user = User.objects.create(username="james", password="password")
# #         obj = Product.objects.create(
# #                                 user=user,
# #                                 name="broom",
# #                                 price=19.99,
# #                                 quantity=1,
# #                                 month=month,
# #         )
        
# #         form = ProductForm(data=obj)
# #         return form
# #         assert True == form.is_valid()