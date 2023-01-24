from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.UserBook)
admin.site.register(models.BookStore)
