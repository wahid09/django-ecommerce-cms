from django.shortcuts import render
from .forms import RegistrationFrom


# Create your views here.

def user_register(request):
    form = RegistrationFrom()

    if request.method == 'POST':
        form = RegistrationFrom(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }
    return render(request, 'account/register.html', context)


def user_login(request):
    return render(request, 'account/user_login.html')


def user_dashboard(request):
    return render(request, 'account/user_dashboard.html')


def delivery_boy_dashboard(request):
    return render(request, 'account/dalivery_boy_dashboard.html')


def seller_dashboard(request):
    return render(request, 'account/seller/home.html')
