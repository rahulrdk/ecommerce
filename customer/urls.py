from django.urls import path
from .import views


app_name='customer'
urlpatterns = [

    path('my_order',views.my_order,name='my_order'),
    path('check_out',views.check_out,name='check_out'),
    path('my_cart',views.my_cart,name='my_cart'),
    path('customer_profile',views.customer_profile,name='customer_profile'),

    
]