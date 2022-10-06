from django.shortcuts import render


# Create your views here.

def user_dashboard(request):
    return render(request, 'account/user_dashboard.html')


def delivery_boy_dashboard(request):
    return render(request, 'account/dalivery_boy_dashboard.html')


def seller_dashboard(request):
    return render(request, 'account/seller/home.html')
