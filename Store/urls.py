# filepath: /c:/Users/Honor/Desktop/SHUDKA44/SHUDKA44/Store/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('customers/<int:customer_id>/make_payment/', views.make_payment, name='make_payment'),
]