# PasteHunter v.10
# Author : Dibyendu Sikdar  
# Credits: 
# Code of Python to scrap urls from results is taken from here... 
# https://raw.githubusercontent.com/getlinksc/scrape_google/master/search.py
import urllib
import requests
from bs4 import BeautifulSoup
from colorama import init
from colorama import Fore, Back, Style

init()

#stores the pastes in raw/ directory
basedir = "raw/"

#CHANGE THE intext: WITH THE INFORMATION YOU WANT TO SEARCH
query = "site:pastebin.com intext:smtp.sendgrid.net"
query = query.replace(' ', '+')


def getContentRaw(url):
    fname = url[url.rindex("/")+1:len(url)]
    url = "https://pastebin.com/raw/"+url[url.rindex("/")+1:len(url)]
    USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"
    headers = {"user-agent": USER_AGENT}
    r = requests.get(url,headers=headers)
    w = open(basedir+fname,'w')
    w.write(r.text)
    w.close()

def beginScraping():
    print(Fore.GREEN+"Starting digging google to find juicy information about "+query)


    #user-agent
    USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"
    headers = {"user-agent": USER_AGENT}

    results = []

    #Searching 10 results results only at a time ( per page returns 10 results )
    #Just querying 1 page to avoid detection/blacklisting, adjust as you want 
    #Change the 2nd parameter with multiple of 10 to scrap pages, like 10, 20, 30, etc
    for start in range(0,10,10):

        pos = str(start)
        URL = f"https://google.com/search?q={query}&start{pos}"
        resp = requests.get(URL, headers=headers)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, "html.parser")
            for g in soup.find_all('div', class_='g'):
                # anchor div
                rc = g.find('div', class_='rc')
                # description div
                s = g.find('div', class_='s')
                if rc:
                    divs = rc.find_all('div', recursive=False)
                    if len(divs) >= 2:
                        anchor = divs[0].find('a')
                        link = anchor['href']
                        results.append(link)

    #Get the results
    for url in results:
        print(Fore.RED+"Fetching contents of "+url)
        getContentRaw(url)

beginScraping()