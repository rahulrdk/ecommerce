from django.urls import path
from .import views


app_name='seller'
urlpatterns = [

    path('seller_home',views.seller_home,name='seller_home'),
    path('add_product',views.add_product,name='add_product'),
    path('seller_password',views.seller_password,name='seller_password'),

    
]