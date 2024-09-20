# admin.py
from django.contrib import admin
from .models import Fertilizer

class FertilizerAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']

admin.site.register(Fertilizer, FertilizerAdmin)
