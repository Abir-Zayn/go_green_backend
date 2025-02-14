from django.contrib import admin
from .models import User
# Register your models here.

# Registering the User model in the admin panel
admin.site.register(User)