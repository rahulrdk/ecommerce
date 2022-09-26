from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def common_page(request):
    return render(request,'common/common_page.html')

def cust_login(request):
    return render(request,'common/cust_login.html')

def seller_login(request):
    return render(request,'common/seller_login.html')

def admin_login(request):
    return render(request,'common/admin_login.html')

def cust_signup(request):
    msg=''
    if request.method == 'POST':
        c_name = request.POST['cust_name']
        c_email = request.POST['cust_email']
        c_phone = request.POST['cust_phone']
        c_password = request.POST['cust_password']
        c_file = request.FILES['cust_file']
        customer_exist=Customer.objects.filter(cust_email=c_email).exists()
        if not customer_exist:

            customer = Customer(cust_name=c_name,cust_phone=c_phone,cust_email=c_email,cust_img=c_file,cust_password=c_password)
            customer.save()
            msg='success'
        else:
            msg='email already exists'
    return render(request,'common/cust_signup.html',{'message':msg})

def seller_signup(request):
    return render(request,'common/seller_signup.html')


    