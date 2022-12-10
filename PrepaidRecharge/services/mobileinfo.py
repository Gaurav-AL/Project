from email.policy import default
import re
import json
import urllib.request
from collections import defaultdict
import math
from bs4 import BeautifulSoup as bs
import requests
import random
import certifi
import urllib3
import phonenumbers
from phonenumbers import carrier , geocoder
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",}

def getHTMLDoc(url):
    response = requests.request("GET", url, headers=headers, verify=False)
    return response.text

'''
Method to getting plans,operator and country of a phone number.
'''
def getInfo(number,operator , circle):
    new_circle = circle.split(" ")
    s = "+".join(new_circle)
    print(number)
    all_plans = getPlan(operator , s)
    try:
        phno = phonenumbers.parse(f"+91{number}")
    except:
        return [all_plans,"Wrong Number"]
    oper = carrier.name_for_number(phno , 'en')
    city = geocoder.description_for_number(phno , "en")
    if(oper == ''):
        oper = f"Wrong Number :( Showing Plans For {operator} in circle {circle} in location {city}"
    elif(not all_plans):
        oper  = f"No operator Found for this Number in {circle} :("
    # print(type(all_plans))
    return [all_plans,oper]
    
'''
Web Scraping for getting Plans
'''
def getPlan(operator , s):
    try:
        getplans = f"https://mplan.in/plans.php?offer=simple&operator={operator}&cricle={s}"
    except:
        return "Unable to Open Url"
    
    string = getHTMLDoc(getplans)
    code = bs(string, 'html.parser')
    
    soup = code.find_all("ul" , {'class' : 'w3ls-plan'})
    all_plans = []
    for i in range(len(soup)):
        amounts = soup[i].find_all("div" , {"class" : "agile-price"})
        desc = soup[i].find_all("div" , {"class" : "valid-agileits"})
        my_dict = defaultdict(dict)
        for j in range(len(amounts)):
            amt = amounts[j].find("span")
            my_dict['amount'] = amt.text
            description = desc[j].find_all("p")
            string = []
            for k in range(len(description)):
                string.append(description[k].text)
            string = ",".join(string)
            my_dict["description"] = string
            all_plans.append(my_dict.copy())
    # print(all_plans)
    return all_plans
            
# getInfo("8090161875" , "Airtel" , "Delhi+NCR")  
    
    



