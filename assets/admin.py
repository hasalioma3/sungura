from django.contrib import admin

from .models import Assets, Category, Location, Staff

# Register your models here.

admin.site.register(Assets)
admin.site.register(Category)
admin.site.register(Staff)
admin.site.register(Location)
