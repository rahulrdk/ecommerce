from django.urls import path
from .import views


app_name='customer'
urlpatterns = [

    path('my_order',views.my_order,name='my_order'),

    
]