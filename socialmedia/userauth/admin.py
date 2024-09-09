from django.contrib import admin

# Register your models here.
from .models import Profile,Student

admin.site.register(Profile)
admin.site.register(Student)
