# Generated by Django 5.1.3 on 2024-12-04 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0002_oyinstatistika_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kurslar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
                ('tavsif', models.TextField()),
                ('narxi', models.DecimalField(decimal_places=2, max_digits=10)),
                ('davomiyligi', models.IntegerField()),
            ],
        ),
    ]