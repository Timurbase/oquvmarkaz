from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta


class OyinNatijasi(models.Model):
    foydalanuvchi = models.OneToOneField(User, on_delete=models.CASCADE)
    urinishlar_soni = models.PositiveIntegerField(default=0)
    bajarilgan_yuz = models.FloatField(default=0.0)

    def yangilash(self, bajarilgan_yuz):
        self.urinishlar_soni += 1
        self.bajarilgan_yuz = bajarilgan_yuz
        self.save()

    def __str__(self):
        return f"{self.foydalanuvchi.username} - {self.bajarilgan_yuz}%"


class OyinStatistika(models.Model):
    foydalanuvchi = models.OneToOneField(User, on_delete=models.CASCADE)
    umumiy_vaqt = models.DurationField(default=timedelta(seconds=0))  # O‘yin o‘ynash vaqti
    umumiy_yutug = models.FloatField(default=0.0)  # O‘yin natijalari
    yuqori_progress = models.FloatField(default=0.0)  # Eng yuqori progress

    def __str__(self):
        return f"{self.foydalanuvchi.username} - {self.umumiy_yutug}%"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_premium = models.BooleanField(default=False)
    trial_end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {'Premium' if self.is_premium else 'Trial'}"


class Kurslar(models.Model):
    nomi = models.CharField(max_length=200)
    tarif = models.TextField()  # Kurs tarifini saqlash
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    davomiyligi = models.IntegerField()

    def __str__(self):
        return self.nomi


class Yangiliklar(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='yangiliklar_images/', null=True, blank=True)  # Rasm
    created_at = models.DateTimeField(auto_now_add=True)  # Yangilik yaratilgan sana

    def __str__(self):
        return self.title


class Loyihalar(models.Model):
    name = models.CharField(max_length=200)  # Loyihaning nomi
    description = models.TextField()  # Loyihaning ta'rifi
    image = models.ImageField(upload_to='loyihalar_images/', null=True, blank=True)  # Rasm
    created_at = models.DateTimeField(auto_now_add=True)  # Loyihaning boshlanish sanasi

    def __str__(self):
        return self.name
