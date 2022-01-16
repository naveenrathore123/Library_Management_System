from django.urls import path

# we have to import views files here to use views.funName.....added manually
from . import views

# we have to give define path for pages....added manually
urlpatterns = [

    path("", views.home, name="home"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("testing", views.testing, name="testing")
]