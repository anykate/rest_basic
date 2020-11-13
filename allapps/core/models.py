from django.db import models


# Create your models here.
class Room(models.Model):
    r_name = models.CharField(max_length=255)

    def __str__(self):
        return self.r_name


class Student(models.Model):
    s_name = models.CharField(max_length=255)
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.s_name
