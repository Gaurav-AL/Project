from sqlite3 import IntegrityError
from django.db import IntegrityError
from django.contrib.messages.api import success
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import userDetail,contactsInfo,billInfo
import datetime


def login(request):
    # print(request.GET)
    return render(request,'form.html')
def isvalid(request,username,email,dob,password,gender,descr):
    flag = 0
    date = datetime.datetime.now().date()
    if(date.year - int(dob.split('-')[0]) < 2):
        flag = 1
        messages.add_message(request, messages.ERROR, "Please Enter Valid Date of Birth")
    if(userDetail.objects.filter(username = username).exists()):
        flag = 1
        messages.add_message(request, messages.ERROR, "Username Already Exists ! Choose different Name ")
    if(len(username) <= 2):
        flag = 1
        messages.add_message(request, messages.ERROR, "Username length should be greater than two")
    if(len(password) <= 6):
        flag = 1
        messages.add_message(request, messages.ERROR, "Please try Stronger password, length greater than 6 may be, not your name") 
    if(descr != None and len(descr.split(" ")) <= 2):
        flag = 1
        messages.add_message(request, messages.ERROR, "Please Describe More Briefly !")
    
    if(flag != 1):
        messages.add_message(request,messages.SUCCESS,"LogIN SuccessFull")
    return flag
    
def getdata(request):
    
    if(request.method == 'POST'):
        username = request.POST['name']
        email = request.POST['email']
        dob = request.POST['dob']
        password = request.POST['pass']
        gender = request.POST['gender']
        descr = request.POST['descr']
        if(isvalid(request,username,email,dob,password,gender,descr) == 0):
            
            user_details = userDetail(username=username,email=email,password = password,dob = dob,descr = descr,gender = gender)
            user_details.save()
            return redirect('/home')
        else:
            return redirect('/login')
    return render(request,"form.html")
def home(request):
    return render(request,"home.html")
def contacts(request):
    if(request.method == "POST"):
        email = request.POST['email']
        phone_no = request.POST['phno']
        query = request.POST['query']

        cont = contactsInfo(email=email,phone_no = phone_no,query = query)
        cont.save()
        messages.add_message(request, messages.SUCCESS, 'Query Has Been Sent Successfully, We will contact You Soon.')
    return render(request,"contacts.html")

def services(request):
    if(request.method == "POST"):
        
        total = 0
        items = ''
        some_var = request.POST.getlist('Pizza[]')
        for values in some_var:
            total += int(values.split("-")[0])
            items += values.split("-")[1] +" "
        name = userDetail.objects.latest('username')
        bill = billInfo(name= name,total=total,Items = items)
        messages.add_message(request,messages.SUCCESS,"Your Order Received !")
        bill.save()
    else:
        return render(request,"form3.html")
    return render(request,"form3.html")

def signup(request):
    if(request.method == "POST"):
        email = request.POST['email']
        password = request.POST['password']
        check_existing = userDetail.objects.filter(email = email).exists() and userDetail.objects.filter(password = password).exists()
        if(check_existing):
            messages.add_message(request, messages.SUCCESS, 'Login SuccessFull',fail_silently=True)
            return redirect('/home')
        else:
            messages.add_message(request, messages.ERROR, 'Wrong Email or Password')
            return redirect('/signup')
    else:
        return render(request,"signup.html")
    
def logout(request):
    return render(request,'form.html')
    

