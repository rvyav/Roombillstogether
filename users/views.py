from django.shortcuts import (
						get_object_or_404,
						render, 
						redirect
)

from django.contrib import messages
from django.contrib.auth import get_user_model
from core.models import Month, Product
from users.forms import EditProfileForm, UserRegistrationForm

from django.views.decorators.cache import cache_page

User = get_user_model()

@cache_page(60 * 15)
def index(request):
	users = User.objects.all()

	context = {'users': users}
	return render(request, 'users/index.html', context)

def profile(request):
	profile = request.user
	months = Month.objects.all()
	product = Product.objects.filter(id__in=months, user=profile).order_by('month')
	context = {'profile': profile, 'months': months}

	return render(request, 'users/profile.html', context)

def profile_expense_detail(request, slug):
	month = get_object_or_404(Month, slug=slug)

	monthly_purchases = [purchases for purchases in month.months.all() if purchases.user == request.user]

	aggregate_purchases = [purchases.price for purchases in month.months.all() if purchases.user == request.user]

	total_price = (sum(aggregate_purchases))

	context = {'month': month, 
			'monthly_purchases': monthly_purchases, 
			'total_price': total_price
	}
	return render(request, 'users/profile-expense-detail.html', context)	

def edit_profile(request, id):
    """Update user profile."""
    user = get_object_or_404(User, id=id)
    form = EditProfileForm(request.POST, request.FILES, instance=user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your account was updated successfully')
        return redirect('users:profile')
    else:
        form = EditProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'users/edit-profile.html', context)

def register(request):
	"""Register user."""
	form = UserRegistrationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('core:month_list')
	else:
		form = UserRegistrationForm()

	context = {'form': form}
	return render(request, 'registration/register.html', context)