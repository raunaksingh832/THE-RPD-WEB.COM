from django.http import request
from django.shortcuts import render,HttpResponse
from datetime import datetime
from django.contrib import messages 
from myapp import models

# Create your views here.
def index(response):
    return render( response,'index.html')      
def about (response):
    return render( response,'about.html')     
def blog(response):
    return render( response,'blog.html')     
def business(response):
    return render( response,'business.html')     
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phonenumber')
        desc = request.POST.get('desc')
        date = datetime.today()
        contact = models.Contact(name=name,email=email,phone_number=phone_number,desc=desc,date=date)
        contact.save()
        messages.success(request, 'YOUR MESSAGE HASS BEEN SUBMITED SUCCESSFULY !!')


    return render( request,'contact.html') 
def covid_19_donation(request):
    return render(request,'covid-19-donation.html') 
def how_to_fight_covid(request):
    return render(request,'How-to-fight-covid.html')   