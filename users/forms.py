from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django import forms
from users.models import CustomUser

User = get_user_model()

class EditProfileForm(ModelForm):
	class Meta:
		model = CustomUser
		fields = [
				'username', 
				'first_name', 
				'last_name',
				'bio',
				'phone_number',
				'gender',
				'profile_picture',
		]

	# def clean_profile_picture(self, *args, **kwargs):
	# 	profile_picture = self.cleaned_data.get('profile_picture')
	# 	valid_extensions = ['jpg', 'jpeg']
	# 	extension = profile_picture.rsplit('.', 1)[1].lower()
	# 	if extension not in valid_extensions:
	# 		raise forms.ValidationError("Only .JPEG and .JPG are allowed")
	# 	return profile_picture


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    first_name = forms.CharField(label='First name', required=False, help_text='Optional')
    last_name = forms.CharField(label='Last name', required=False, help_text='Optional')
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'password2'
        ]

    def clean(self, *args, **kwargs):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Passwords must match")
        return super(UserRegistrationForm, self).clean(*args, **kwargs)

    def save(self, commit=True):
        # Hash password		
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
           user.save()
        return user


