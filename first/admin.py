from django.contrib import admin

# we need to import our model from our app..... Added Manually
from first.models import Example
from first.models import Contact


# Register your models here.

# we need to register our model..... Added Manually
admin.site.register(Example)
admin.site.register(Contact)

