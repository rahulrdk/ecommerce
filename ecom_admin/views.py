from django.shortcuts import render

# Create your views here.

def admin_home(request):
    return render(request,'ecom_admin/admin_home.html')

def approve_seller(request):
    return render(request,'ecom_admin/approve_seller.html')

def view_seller(request):
    return render(request,'ecom_admin/view_seller.html')

def view_customer(request):
    return render(request,'ecom_admin/view_customer.html')
