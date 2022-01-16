from django.contrib import admin

# we need to import our model from our app..... Added Manually
from need.models import BookCollection, StudentRecord, BookRecord, HistoryRecord


# Register your models here.

# we need to register our model..... Added Manually
admin.site.register(BookCollection)
admin.site.register(StudentRecord)
admin.site.register(BookRecord)
admin.site.register(HistoryRecord)

