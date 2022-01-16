from django.shortcuts import render, redirect
from django.http import HttpResponse

# importing for passing todays date to our model...added manually
# from datetime import datetime

# we have to import our models from model file of app for initialising objects
from first.models import Example
from first.models import Contact

from django.contrib import messages


# Create your views here.


# creating home function and call home.html page.....added manually
def home(request):
    return render(request, 'home.html')


# contact function...added manually
def contact(request):

    # if request is POST then fetch all data from contact.html form

    if request.method == "POST":

        # fetching all datas

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        text = request.POST.get('text')

        # initializing contact object  to save all information in our Contact model or in database

        contact = Contact(name=name, email=email, phone=phone, text=text)
        contact.save()
        
        # or
        # method to save enties in our database....we have to pass object name in save
        # Contact.save(contact)

        messages.success(request, "We received your Concern, our Representation will reach to you soon..")

        return redirect("/")

    else:
        
        return render(request, 'contact.html')     


# about function.....added manually
def about(request):
    return render(request, 'about.html')


def testing(request):

    if request.method == "POST":

        name = request.POST.get('name')
        age = request.POST.get('age')

        example = Example(name=name, age=age)

        # method to save enties in our database....we have to pass object name in save
        Example.save(example)

        messages.success(request, "Testing performed Successfully..")

        return redirect("/")


    else:
        
        return render(request, 'testing.html')    
        