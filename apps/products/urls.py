from django.urls import path 

from .views import *

urlpatterns = [
    path('product/', products, name='product'),
    path('product_detail/<int:id>/', product_detail, name='product_detail'),
    path('search/', search, name='search'),
]