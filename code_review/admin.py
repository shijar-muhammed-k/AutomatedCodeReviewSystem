from django.contrib import admin

from .models import tempFile, Code
# Register your models here.
admin.site.register(Code)
admin.site.register(tempFile)