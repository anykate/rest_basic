from django.contrib import admin
from .models import Room, Student


# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['r_name']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 's_name']
