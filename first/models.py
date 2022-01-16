from django.db import models

# import this for saving date and time....added manually
# from django.utils import timezone

# Create your models here.


# creating Example model....added manually

class Example(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    
    # displaying by name in our database instaed of (ModelName Object 1)
    def __str__(self):
        return self.name


# creating Contact model....added manually

class Contact(models.Model):

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    text = models.TextField()

    # we have to give some default value..for more info see django documentations
    # date = models.DateField(default=timezone.now())

    # displaying by name in our database instaed of (ModelName Object 1)
    def __str__(self):
        return self.name