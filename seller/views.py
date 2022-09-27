from django.shortcuts import render

# Create your views here.


def seller_home(request):
    return render(request,'seller/seller_home.html')

def add_product(request):
    return render(request,'seller/add_product.html')

def seller_password(request):
    return render(request,'seller/seller_password.html')