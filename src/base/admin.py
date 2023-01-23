from django.contrib import admin
from .models import ReadBooks, UnreadBooks 

# Register your models here.

admin.site.register(ReadBooks)
admin.site.register(UnreadBooks)
