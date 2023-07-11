from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def projects(request):
    return HttpResponse("this is projects page")

def cv(request):
    return HttpResponse("this is cv page")

def contact(request):
    return HttpResponse("this is contact page") 