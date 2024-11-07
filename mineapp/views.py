from django.shortcuts import render
from django.template.context_processors import request


# Create your views here.
def home(request):
    return render(request, 'index.html')
def abt(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contactus.html')
def heo(request):
    return render(request, 'blog.html')
def serv(request):
    return render(request, 'services.html')
def assin(request):
    return render(request,'assignment.html')