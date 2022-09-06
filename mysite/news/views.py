from django.shortcuts import render
from django.http import HttpResponse
from .models import News

def index(request):
    #сортируем в обратном порядке ( знак минус )
    news = News.objects.all
    return render(request, 'news/index.html', {'news' : news, 'title' : 'Список новостей'})
