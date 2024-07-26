# users/admin.py
from django.contrib import admin
from .models import User  # Replace User with your model names

admin.site.register(User)  # Register your models here
