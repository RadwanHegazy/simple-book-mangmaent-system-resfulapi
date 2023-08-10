from django.contrib import admin
from .models import Book, Category
from django.contrib.auth.models import Group



admin.site.register(Book)
admin.site.register(Category)



admin.site.unregister(Group)