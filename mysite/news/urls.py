from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index),
    path('category/<int:category_id>/', get_category) #параметр url-запроса
]