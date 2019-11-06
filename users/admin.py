from django.contrib import admin
# AbstractUser not hashing password
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser
#admin.site.register(CustomUser, UserAdmin)

# New Customized User Admin
#admin.site.register(CustomUser)

@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    list_display = [
                'username', 
                'email',
                'first_name', 
                'last_name', 
                'bio', 
                'phone_number',
                'is_host',
                'gender'
    ]

    list_filter = [
                'username', 
                'email',
                'first_name', 
                'last_name',
                'phone_number',
    ]

    list_editable = [
                'first_name', 
                'last_name',
                'email', 
                'bio', 
                'phone_number',
                'is_host',
                'gender'
    ]