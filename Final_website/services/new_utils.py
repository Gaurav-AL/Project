from collections import defaultdict

from bs4 import BeautifulSoup as bs
import requests
import random
import certifi
import urllib3


page_number = random.randint(1,880)
# print(page_number)
source = f"https://www.technewsworld.com/archive/page/{page_number}"
googlenews = {
"googlebusinessNew":"https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen",
"googletechnologyNews" :"https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen",
"googleEntertainmentsNews":"https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNREpxYW5RU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen",
"googlesportsNews" : "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen",
"googlescienceNews" :"https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp0Y1RjU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen",
"googlehealthNews"  :"https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen"
}
headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    }
urllib3.disable_warnings()
def getBusinessData(text):
    text = bs(text, 'html.parser')
    news = text.find("div",{"class":"XlKvRb"})
    print(news)
    
    
def getGoogleNews(source):
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
    for key,value in source.items():
        business = http.request("GET", source["googlebusinessNew"],timeout=4.0,headers={"Accept-Encoding": "br"}).data
        getBusinessData(business)
        # technology = http.request("GET", source["googletechnologyNews"],timeout=4.0,headers={"Accept-Encoding": "br"}).data
        # entrertainment = http.request("GET", source["googleEntertainmentsNews"],timeout=4.0,headers={"Accept-Encoding": "br"}).data
        # sports = http.request("GET", source["googlesportsNews"],timeout=4.0,headers={"Accept-Encoding": "br"}).data
        # science = http.request("GET", source["googlescienceNews"],timeout=4.0,headers={"Accept-Encoding": "br"}).data
        # health = http.request("GET", source["googlehealthNews"],timeout=4.0,headers={"Accept-Encoding": "br"}).data
    
# getGoogleNews(googlenews)    

def getHTMLDoc(url):
    response = requests.request("GET", url, headers=headers, verify=False)
    return response.text

def geturl(url):
    code_html =  bs(getHTMLDoc(url), 'html.parser')
    
    news = code_html.find("div",{"class":"more-articles category-article-list"})
    news = news.find_all("a")
    
    links = set()
    images = []
    headings = []
    for i in range(len(news)):
        links.add(news[i].get("href"))
        if(news[i].find("img") != None):
            images.append(news[i].find("img").get("src"))
        if(news[i].find("h2") != None):
            headings.append(news[i].find("h2"))
        
    links = list(links)
    tnews = []
    # print(len(links),len(headings),len(images))
    for i in range(len(links)):
        if(i < len(links) and i < len(headings) and i < len(images)):
            tnews.append([links[i],images[i],headings[i].text])
    # print(tnews)    
    return tnews

# geturl(source)
        
    

     
        