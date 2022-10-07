from django.shortcuts import render
from category.models import Category

# Create your views here.


def home(request):
    """
    Home page with the product information
    """
    return render(request, 'ecommerce/home.html')


def cart_detail_view(request):
    """
    Load product information with modal when user click add to cart button in home page
    """
    return render(request, 'ecommerce/cart_detail.html')


def category_product_list(request):
    """
    Show all category wise product list with filters options
    """
    return render(request, 'ecommerce/category_product_list.html')


def single_product_view(request):
    """
    Show single product information
    """
    return render(request, 'ecommerce/single_product_view.html')