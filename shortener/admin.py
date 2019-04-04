from django import forms
from django.contrib import admin

# Register your models here.

from shortener import models


class ShorcutAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

    def id(self, obj):
        return f'id to jest rowne: {obj.id}'



admin.site.register(models.Shortcut, ShorcutAdmin)
