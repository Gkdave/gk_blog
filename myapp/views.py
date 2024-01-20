from django.shortcuts import render
from django.http import HttpResponse 
from datetime import datetime
from .models import Blog 

# Create your views here.
def index(request):
    
    blog = Blog.objects.all()
    return render(request,'home.html',{'blog':blog})
  
def user_register(request):
  return render(request,'register.html')