from django.shortcuts import render
from django.http import HttpResponse 
from datetime import datetime

# Create your views here.
def index(request):
    date=datetime.today()
    context = {
      'name': "gajendra",
      'date': date
        
    }
    
    return render(request,'home.html',context)