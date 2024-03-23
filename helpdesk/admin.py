from django.contrib import admin
from helpdesk import models

# Register your models here.

@admin.register(models.Call)
class HelpdeskAdmin(admin.ModelAdmin):
    list_display = 'id', 'title',
    ordering = '-id',
    list_per_page = 10
    #list_display_links = 'title'


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'id',

