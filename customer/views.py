from django.shortcuts import render

# Create your views here.

def my_order(request):
    return render(request,'customer/my_order.html')

def check_out(request):
    return render(request,'customer/check_out.html')

def my_cart(request):
    return render(request,'customer/my_cart.html')
