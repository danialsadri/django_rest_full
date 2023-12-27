from django.contrib import admin
from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'year']
    list_filter = ['year']
    search_fields = ['name']
