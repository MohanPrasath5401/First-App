from django.contrib import admin
from .models import Profile

# Register your models here.

@admin.register(Profile)
class Profile_data(admin.ModelAdmin):
    list_display = ["age","image"] # fields to be display in django admin page



