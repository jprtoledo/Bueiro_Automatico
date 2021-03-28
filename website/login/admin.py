from django.contrib import admin
from .models import datalog

# Register your models here.

@admin.register(datalog)
class DatalogAdmin(admin.ModelAdmin):
    # Colocar todas as colunas abaixo no site
    list_display = ('is_active', 'device_name', 'last_occurrence')

    