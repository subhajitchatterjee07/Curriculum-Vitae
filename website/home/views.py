from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')

def projects(request):
    return render(request,'projects-grid-cards.html')

def cv(request):
    return render(request,'cv.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name,subject=subject,email=email,message=message,date=datetime.today())
        contact.save()
        messages.success(request,'Your Message has been sent.')
    return render(request,'contact.html') 