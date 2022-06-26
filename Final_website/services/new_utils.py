from bs4 import BeautifulSoup as bs
import requests
import re

source = "https://www.technewsworld.com/"



def getHTMLDoc(url):
    response = requests.get(url)
    return response.text

def geturl(url):
    code_html =  bs(getHTMLDoc(url), 'html.parser')
    print(code_html)

geturl(source)