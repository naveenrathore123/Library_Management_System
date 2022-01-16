from django.urls import path

# we have to import views files here to use views.funName.....added manually
from . import views

# we have to give define path for pages....added manually
urlpatterns = [

    path("catalog", views.catalog, name="catalog"),
    path("search", views.search, name="search"),
    path("IssueConfirmation", views.IssueConfirmation, name="IssueConfirmation"),
    path("askIssue", views.askIssue, name="askIssue"),
    path("Issue", views.Issue, name="Issue"),
    path("reIssue", views.reIssue, name="reIssue"),
    path("Return", views.Return, name="Return")

]