from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import PasswordChangeForm

from datetime import datetime
from django.core.mail import send_mail
from . models import Blog 
from . forms import Edit_blog 

# Create your views here.
def index(request):
    
    blog = Blog.objects.all()
    return render(request,'home.html',{'blogs':blog})
  
def user_register(request):

  if request.method == 'POST':
    fname=request.POST.get('firstname')
    lname=request.POST.get('lastname')
    uname=request.POST.get('username')
    email=request.POST.get('email')
    pass1=request.POST.get('password1')
    pass2=request.POST.get('password2')
    if pass1 != pass2:
      messages.warning(request,'password does not match')
      return redirect('register')
    
    elif User.objects.filter(username=uname).exists():
      messages.warning(request,'email already taken')
      return redirect('register')
    else:
      user = User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=pass1)
      user.save()
      messages.success(request, "User has been registered successfully")
      return redirect('login')
      
  return render(request,'register.html')

def user_login(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request,username=username,password=password)
    if user is not None:
      login(request,user)
      return redirect('/')
    else:
      messages.warning(request,'Invalid Credentials')
      return redirect('login')
  return render(request,'login.html')
    
def user_logout(request):
    logout(request)
    return redirect('/')
  
def post_blog(request):
  if request.method == 'POST':
    title = request.POST.get('title')
    desc = request.POST['desc']
    
    if title is None:
      return redirect('/')
    else:
      blog = Blog(title=title,desc=desc,user_id=request.user)
      blog.save()
      messages.success(request,"blog post has been successfully")
      return redirect('/')
    
  return render(request,'blog_post.html')

def blog_detail(request,id):
  blog = Blog.objects.get(id=id)
  context = {
    'blog' : blog 
  }
  return render(request,'blog_detail.html',context)
def delete(request,id):
  blog = Blog.objects.get(id=id)
  blog.delete()
  messages.success(request,"Post has been deleted successfully")
  return redirect('/')

def edit(request,id):
  blog = Blog.objects.get(id=id)
  editblog = Edit_blog(instance=blog)
  
  if request.method == "POST":
    form = Edit_blog(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,"post has been Updated")
      return redirect('/')
    
  return render(request,'edit_blog.html',{'edit_blog': editblog})
  
def change_password(request):
  if request.method=="POST":
    form = PasswordChangeForm(request.user,request.POST)
    if form.is_valid():
      form.save()
      #update_session_auth_hash(request, user)
      messages.success(request,"Your password has been changed")
      return redirect('/')
    else:
      messages.warning(request,'Error')
      return redirect("change_password")
  else:
    form = PasswordChangeForm(request.user)
    return render(request,'change_password.html',{ 'PasswordChangeForm':form})


  


  