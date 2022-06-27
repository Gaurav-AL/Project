from collections import defaultdict

from bs4 import BeautifulSoup as bs
import requests
import random


page_number = random.randint(1,880)
print(page_number)
source = f"https://www.technewsworld.com/archive/page/{page_number}"



def getHTMLDoc(url):
    response = requests.get(url)
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
        tnews.append([links[i],images[i],headings[i].text])
    # print(tnews)    
    return tnews

# geturl(source)
        
    

     
        