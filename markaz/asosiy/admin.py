from django.contrib import admin
from .models import OyinStatistika, Kurslar
from .models import Yangiliklar, Loyihalar
from django.utils.html import format_html

# OyinStatistikaAdmin klassi
class OyinStatistikaAdmin(admin.ModelAdmin):
    list_display = ('id', 'umumiy_vaqt', 'oyinlar_soni')  # Oyinlar sonini ko‘rsatish

    def oyinlar_soni(self, obj):
        return obj.oyinlar_soni


class KurslarAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'narxi', 'davomiyligi', 'tasvir_preview')
    search_fields = ('nomi',)
    list_filter = ('davomiyligi',)

    def tasvir_preview(self, obj):
        if obj.tasvir:
            return format_html('<img src="{}" width="100" />', obj.tasvir.url)
        return 'Tasvir yo‘q'

    tasvir_preview.short_description = 'Tasvir'

    tasvir_preview.allow_tags = True
    tasvir_preview.short_description = 'Tasvir'


admin.site.register(OyinStatistika, OyinStatistikaAdmin)
admin.site.register(Kurslar, KurslarAdmin)

class YangiliklarAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Yangiliklar sarlavhasi va sanasi
    search_fields = ('title',)  # Sarlavha bo‘yicha qidirish
    list_filter = ('created_at',)  # Sanaga qarab filtrlar

class LoyihalarAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')  # Loyihaning nomi va sanasi
    search_fields = ('name',)  # Loyihalar nomi bo‘yicha qidirish
    list_filter = ('created_at',)  # Sanaga qarab filtrlar

admin.site.register(Yangiliklar, YangiliklarAdmin)
admin.site.register(Loyihalar, LoyihalarAdmin)