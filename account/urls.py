from django.urls import path
from .views import user_dashboard, delivery_boy_dashboard, seller_dashboard


app_name = "App_Account"

urlpatterns = [
    path('user-dashboard/', user_dashboard, name='user_dashboard'),
    path('delivery-boy-dashboard', delivery_boy_dashboard, name='delivery_boy_dashboard'),
    path('seller-dashboard', seller_dashboard, name='seller_dashboard'),
]