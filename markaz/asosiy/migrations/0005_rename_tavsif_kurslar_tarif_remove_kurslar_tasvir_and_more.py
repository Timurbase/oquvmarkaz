# Generated by Django 5.1.3 on 2024-12-05 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0004_loyihalar_yangiliklar_kurslar_tasvir'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kurslar',
            old_name='tavsif',
            new_name='tarif',
        ),
        migrations.RemoveField(
            model_name='kurslar',
            name='tasvir',
        ),
        migrations.AlterField(
            model_name='kurslar',
            name='nomi',
            field=models.CharField(max_length=200),
        ),
    ]
