from django.urls import path

# we have to import views files here to use views.funName.....added manually
from . import views

# we have to give define path for pages....added manually
urlpatterns = [

    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout")
]