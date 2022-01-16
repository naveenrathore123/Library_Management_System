from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class StudentInfo(models.Model):

    phone = models.CharField(max_length=20)
    rollNumber = models.CharField(max_length=20)
    user_Id = models.OneToOneField(User, on_delete=models.CASCADE, related_name="detail")

    def __str__(self):
        return self.rollNumber
