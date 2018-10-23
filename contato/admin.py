# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email']
    search_fields = ['name','email']
    list_filter = ['created']

admin.site.register(Contact,ContactAdmin)