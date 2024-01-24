from django.shortcuts import render
from .models import Product


def product(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})


def employees(request):
    employes = employees.objects.all()
    context = {
        'employes': employes,
    }
    return render(request, 'main/employees.html', context)
