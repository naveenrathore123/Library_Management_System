from django.db import models

# added manually for Due Date in StudentRecord Model
from datetime import datetime, timedelta

# Create your models here.

# creating BookCollection model....added manually

class BookCollection(models.Model):

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    quantity = models.IntegerField()
    
    # displaying by name in our database instaed of (ModelName Object 1)
    def __str__(self):
        return self.name


class StudentRecord(models.Model):
    
    rollNumber = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    
    
    # displaying by name in our database instaed of (ModelName Object 1)
    def __str__(self):
        return self.rollNumber


class BookRecord(models.Model):

    bookName = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    Issuedate = models.DateTimeField(auto_now_add = True, auto_now = False)
    DueDate = models.DateTimeField(default = datetime.now() + timedelta(days = 15))
    BookStatus = models.CharField(max_length=10, default = "False")
    key = models.ForeignKey(StudentRecord, on_delete=models.CASCADE, related_name="books")


    # displaying by name in our database instaed of (ModelName Object 1)
    def __str__(self):
        return self.bookName

class HistoryRecord(models.Model):

    bookName = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    Issuedate = models.DateTimeField()
    DueDate = models.DateTimeField()
    ReturnDate = models.DateTimeField(default=datetime.now())
    BookStatus = models.CharField(max_length=10, default="True")
    Fine = models.IntegerField(default=0)
    Comment = models.CharField(max_length=200, default="Good")
    IdKey = models.ForeignKey(StudentRecord, on_delete=models.CASCADE,related_name="history")

    def __str__(self):
        return self.bookName
    




