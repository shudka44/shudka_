# filepath: /c:/Users/Honor/Desktop/SHUDKA44/SHUDKA44/Store/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Customer, Purchase, Payment
from django.views.decorators.http import require_POST
from decimal import Decimal

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    purchases = Purchase.objects.filter(customer=customer)
    payments = Payment.objects.filter(customer=customer)
    return render(request, 'customer_detail.html', {
        'customer': customer,
        'purchases': purchases,
        'payments': payments,
    })

@require_POST
def make_payment(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    amount = Decimal(request.POST['amount'])
    Payment.objects.create(customer=customer, amount=amount)
    customer.debt -= amount
    customer.save()
    return redirect('customer_detail', customer_id=customer.id)