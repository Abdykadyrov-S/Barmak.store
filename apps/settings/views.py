from django.shortcuts import render, redirect

from .models import *
from apps.products.models import Category, Product
from apps.telegram.views import get_text


# Create your views here.
def index(request):
    settings = Settings.objects.latest('id')
    about = About.objects.latest('id')
    categories = Category.objects.all()
    products = Product.objects.all().order_by('?')
    best_product = Product.objects.all().order_by('?')[:1]
    return render(request, "base/index.html",locals())

def about(request):
    settings = Settings.objects.latest('id')
    about = About.objects.latest('id')
    best_products = Product.objects.all().order_by('?')
    return render(request, "base/about.html",locals())

def contact(request):
    settings = Settings.objects.latest('id')
    about = About.objects.latest('id')
    if request.method =="POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        cause = request.POST.get('cause')
        Contact.objects.create(name=name, phone=phone, message=message, cause=cause)

        get_text(f""" Оставлен отзыв 
Имя пользователя: {name}
Номер телефона: {phone}
Причина: {cause}
Сообщение: {message}
""")
        return redirect('index')

    return render(request, "base/contact.html", locals())