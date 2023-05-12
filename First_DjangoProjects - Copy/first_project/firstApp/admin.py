from django.contrib import admin
from .models import MasterData, Student
# Register your models here.
#admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=["stuid","stuname","stumail","stuclass"]
    
@admin.register(MasterData)
class StudentAdmin(admin.ModelAdmin):
    list_display=["stuid","stuname","stumail","subject"]