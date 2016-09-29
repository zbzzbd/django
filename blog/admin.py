# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Article
# Register your models here.
class ArtileAdmin(admin.ModelAdmin):
    list_display = ('title','update_time')
admin.site.register(Article,ArtileAdmin)

