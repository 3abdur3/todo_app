from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ['item', 'completed']
