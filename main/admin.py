from django.contrib import admin
from .models import article_form, tags

# Register your models here.
admin.site.register(article_form)
admin.site.register(tags)