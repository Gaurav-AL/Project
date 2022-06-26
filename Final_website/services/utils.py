from bs4 import BeautifulSoup as bs
import requests
import re

from django.db.models import Q


source = {
        0:{
        "Country" : "India",
        "Country_Code" : "IND",
        "source" : "https://www.mohfw.gov.in/",
        "type" : "HTML"
        },

        1:{
        "Country" : "China",
        "Country_Code" : "CN",
        "source" : "https://covid19.who.int/region/wpro/country/cn",
        "type" : "HTML"
        },
        2: {
        "Country" : "Pakistan",
        "Country_Code" : "PK",
        "source" : "https://covid19.who.int/region/emro/country/pk",
        "type" : "HTML"
        },
        3 :{
        "Country" : "Bhutan",
        "Country_Code" : "BT",
        "source" : "https://covid19.who.int/region/searo/country/bt/",
        "type" : "HTML"
        },
        4 : {
        "Country" : "Japan",
        "Country_Code" : "JP",
        "source" : "https://covid19.who.int/region/wpro/country/jp",
        "type" : "HTML"
        },
        5 : {
        "Country" : "Indonesia",
        "Country_Code" : "ID",
        "source" : "https://covid19.who.int/region/searo/country/id",
        "type" : "HTML"
        },
        6 : {
        "Country" : "Bangladesh",
        "Country_Code" : "BD",
        "source" : "https://covid19.who.int/region/searo/country/bd",
        "type" : "HTML"
        },
        7 : {
        "Country" : "Turkey",
        "Country_Code" : "TR",
        "source" : "https://covid19.who.int/region/euro/country/tr",
        "type" : "HTML"
        },
        8 : {
        "Country" : "Nepal",
        "Country_Code" : "NP",
        "source" : "https://covid19.who.int/region/searo/country/np",
        "type" : "HTML"
        },
        9 : {
        "Country" : "Malaysia",
        "Country_Code" : "MY",
        "source" : "https://covid19.who.int/region/wpro/country/my",
        "type" : "HTML"
        },
        10 : {
        "Country" : "Qatar",
        "Country_Code" : "QA",
        "source" : "https://covid19.who.int/region/emro/country/qa",
        "type" : "HTML"
        },
        11 : {
        "Country" : "South Korea",
        "Country_Code" : "KP",
        "source" : "https://covid19.who.int/region/searo/country/kp",
        "type" : "HTML"
        },
        12 : {
        "Country" : "Afghanistan",
        "Country_Code" : "AF",
        "source" : "https://covid19.who.int/region/emro/country/af",
        "type" : "HTML"
        },
        13 : {
        "Country" : "Israel",
        "Country_Code" : "IL",
        "source" : "https://covid19.who.int/region/euro/country/il",
        "type" : "HTML"
        },
        14 : {
        "Country" : "Maldives",
        "Country_Code" : "MV",
        "source" : "https://covid19.who.int/region/searo/country/mv",
        "type" : "HTML"
        },
        15 : {
        "Country" : "Oman",
        "Country_Code" : "OM",
        "source" : "https://covid19.who.int/region/emro/country/om",
        "type" : "HTML"
        },
        16 : {
        "Country" : "Laos",
        "Country_Code" : "LA",
        "source" : "https://covid19.who.int/region/wpro/country/la",
        "type" : "HTML"
        },
        17 : {
        "Country" : "Syria",
        "Country_Code" : "SY",
        "source" : "https://covid19.who.int/region/emro/country/sy",
        "type" : "HTML"
        },
        18 : {
        "Country" : "Yemen",
        "Country_Code" : "YE",
        "source" : "https://covid19.who.int/region/emro/country/ye",
        "type" : "HTML"
        },
        19 : {
        "Country" : "Jordan",
        "Country_Code" : "JO",
        "source" : "https://covid19.who.int/region/emro/country/jo",
        "type" : "HTML"
        },
        20 : {
        "Country" : "Mongolia",
        "Country_Code" : "MN",
        "source" : "https://covid19.who.int/region/wpro/country/mn",
        "type" : "HTML"
        }
}

def getHTMLDoc(url):
    response = requests.get(url)
    return response.text

def getWExtractedData(country,url):
    
    code_html =  bs(getHTMLDoc(url), 'html.parser')
     
   
    matrix_wrapper= code_html.find_all(attrs={"data-id":"metric"})
    # today = code_html.find_all("span",{"data-id":"metric"})
    # print(today)
    cumulative_cases = matrix_wrapper[0].text
    cumulative_deaths = matrix_wrapper[1].text
    cumulative_vaccination = code_html.find("p").find_all("span")[-1].text.split(" ")[0].strip()
    date = code_html.find("p").find_all("span")[2].text.split(",")[1].strip()
    return {"date":date,"CumulativeCases":cumulative_cases,"cumulative_deaths":cumulative_deaths,"cumulative_vaccination":cumulative_vaccination}

    
    
    

'''To get India Data  from mygov'''
def getIExtractedData(country,url):
    value = []

    code_html = bs(getHTMLDoc(url),'html.parser')
    date = code_html.find("table", {"class": "statetable table table-striped"})
    date = date.find("span")
    date = date.text.split(":")[1].split(",")[0].strip()
    today = code_html.find("span",{"class":"up"})
    today = today.text.split("<")[0].split("(")[1].split(")")[0]
    
    confirmed_cases = code_html.find("li", {"class": "bg-blue"})
    recovered_cases = code_html.find("li",{"class":"bg-green"})
    deaths = code_html.find("li",{"class":"bg-red"})
    
    confirmed_cases = confirmed_cases.find_all("strong",{"class":"mob-hide"})
    recovered_cases = recovered_cases.find_all("strong",{"class":"mob-hide"})
    deaths = deaths.find_all("strong",{"class":"mob-hide"})
    temp = code_html.find("div", {"class":"col-xs-8 site-stats-count sitetotal"})
    cumulative_vaccination = temp.find_all("span")[1].text.strip()
    today_vaccination = temp.find_all("span")[-1].text.split(" ")[1].split("(")[1]
    
    cc,rc,dt = 0,0,0
    for x in confirmed_cases:
        if(re.search("[0-9]",x.text)):
            cc = x.text.split('\xa0')[0]
    
    for x in recovered_cases:
        if(re.search("[0-9]",x.text)):
            rc = x.text.split('\xa0')[0]
    
    for x in deaths:
        if(re.search("[0-9]",x.text)):
            dt = x.text.split('\xa0')[0]
        
    return {"date":date,"today":today,"Active":cc,"CumulativeDeaths":dt,"RecoveredCases":rc,"cumulative_vaccination":cumulative_vaccination,"today_vaccination":today_vaccination}
    

def getdata():
    countries = []
    date = []
    active  = 0
    today = 0
    recovered  = 0
    vaccination_today = 0
    cumulative_cases = []
    cumulative_deaths = []
    cumulative_vaccinations = []
    
    for key,value in source.items():
        if(value['Country'] == "India"):
            countries.append(value["Country"])
            temp = getIExtractedData(value["Country"],value["source"])
            date.append(temp["date"])
            cumulative_deaths.append(temp["CumulativeDeaths"])
            cumulative_vaccinations.append(temp["cumulative_vaccination"])
            today = temp['today']
            active = temp['Active']
            recovered = temp['RecoveredCases']
            today_vaccine = temp["today_vaccination"]
            
        else:
            countries.append(value["Country"])
            temp = getWExtractedData(value["Country"],value['source'])
            date.append(temp["date"])
            cumulative_cases.append(temp["CumulativeCases"])
            cumulative_deaths.append(temp["cumulative_deaths"])
            cumulative_vaccinations.append(temp["cumulative_vaccination"])
            
            
    return {"overall":[countries,cumulative_deaths,cumulative_vaccinations,date],"india":[today,active,recovered,today_vaccine],"ExceptIndia" :cumulative_cases}
# print(getWExtractedData("China",'https://covid19.who.int/region/wpro/country/cn'))
# print(getIExtractedData("India","https://www.mohfw.gov.in/"))
# print(getHTMLDoc("https://covid19.who.int/region/wpro/country/jp"))

# print(getdata())


