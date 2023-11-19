from django.shortcuts import render
from django.db.models import Q

from apps.settings.models import Settings, About
from .models import Product, Category

# Create your views here.
def products(request):
    categories = Category.objects.all()
    settings = Settings.objects.latest('id')
    products = Product.objects.all().order_by('?')
    about = About.objects.latest('id')
    return render(request, 'shop/products.html', locals())

def product_detail(request, id):
    settings = Settings.objects.latest('id')
    product = Product.objects.get(id=id)
    about = About.objects.latest('id')
    return render(request, 'shop/product_detail.html', locals())

def search(request):
    setting = Settings.objects.latest('id')
    query = request.POST.get('query', '')
    if query:
        # Используйте Q-объекты для выполнения поиска в моделях Shop и Product
        products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'shop/foods.html', locals())