from django.urls import path
from .import views


app_name='common'
urlpatterns = [

    path('',views.common_page,name='common_page'),
    path('cust_login',views.cust_login,name='cust_login'),
    path('seller_login',views.seller_login,name='seller_login'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('cust_signup',views.cust_signup,name='cust_signup'),
    path('seller_signup',views.seller_signup,name='seller_signup'),
    
]