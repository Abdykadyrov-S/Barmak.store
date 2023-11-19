from django.shortcuts import render
from .models import *
from apps.settings.models import Settings, About

# Create your views here.
def news(request):
    settings = Settings.objects.latest('id')
    about = About.objects.latest('id')
    news = News.objects.all() 
    return render(request, "blog/blog.html",locals())

def news_detail(request,id):
    settings = Settings.objects.latest('id')
    about = About.objects.latest('id')
    news_others = News.objects.all().order_by('?')[:2]
    news = News.objects.get(id=id)
    return render(request, "blog/blog-single.html",locals())