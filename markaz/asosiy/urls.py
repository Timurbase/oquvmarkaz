from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin paneliga ulanish
    path('', views.bosh_sahifa, name='bosh_sahifa'),
    path('kurslar/', views.kurslar, name='kurslar'),
    path('narxlar/', views.narxlar, name='narxlar'),
    path('biz_haqimizda/', views.biz_haqimizda, name='biz_haqimizda'),
    path('oyin/', views.oyin_view, name='oyinlar'),  # Bu yerda 'oyin' nomini 'oyinlar' ga o'zgartirdik
    path('accounts/signup/', views.royxatdan_otish, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),  # Django auth tizimini o'z ichiga olgan URL-lar
    path('logout/', views.tizimdan_chiq, name='logout'),
]
