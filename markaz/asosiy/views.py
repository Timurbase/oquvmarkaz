from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Yangiliklar, Loyihalar, Kurslar, OyinNatijasi, OyinStatistika, UserProfile

def bosh_sahifa(request):
    yangiliklar = Yangiliklar.objects.all().order_by('-created_at')  # Yangiliklarni olish
    loyihalar = Loyihalar.objects.all().order_by('-created_at')  # Loyihalarni olish
    return render(request, 'asosiy/bosh_sahifa.html', {'yangiliklar': yangiliklar, 'loyihalar': loyihalar})

def kurslar(request):
    kurslar = Kurslar.objects.all()  # Barcha kurslarni olish
    return render(request, 'asosiy/kurslar.html', {'kurslar': kurslar})

def narxlar(request):
    return render(request, 'asosiy/narxlar.html')

def biz_haqimizda(request):
    return render(request, 'asosiy/biz_haqimizda.html')

def royxatdan_otish(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Foydalanuvchi ro‘yxatdan o‘tishda, sinov muddati uchun vaqt qo‘shish
            user_profile, created = UserProfile.objects.get_or_create(user=user)
            if created:
                user_profile.trial_end_date = datetime.now() + timedelta(days=10)  # Sinov muddati 7 kun
                user_profile.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def oyin_view(request):
    return render(request, 'asosiy/oyinlar.html')

def tizimdan_chiq(request):
    logout(request)
    return redirect('bosh_sahifa')
