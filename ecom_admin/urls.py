from django.urls import path
from .import views


app_name='ecom_admin'
urlpatterns = [

    path('admin_home',views.admin_home,name='admin_home'),
    path('approve_seller',views.approve_seller,name='approve_seller'),
    path('view_seller',views.view_seller,name='view_seller'),
    path('view_customer',views.view_customer,name='view_customer'),

    
]