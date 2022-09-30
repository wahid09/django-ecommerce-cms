from django.urls import path
from ecommerce import views

app_name = "App_Ecommerce"

urlpatterns = [
    path('', views.home, name="home"),
    path('category-product', views.category_product_list, name="category_product"),
    path('product-detail-view', views.cart_detail_view, name="product_cart_view"),
    path('single-product-view', views.single_product_view, name="single_product"),
]