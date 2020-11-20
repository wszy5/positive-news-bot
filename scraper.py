from bs4 import BeautifulSoup as soup
import requests

def main_news():

    site = requests.get("https://dobrewiadomosci.net.pl")
    content = soup(site.content,'html.parser')

    body = content.find("div", {"class": "default-news"})
    news = body.find_all("span",{"class":"comments"})
    arr = []
    for i in news:
        arr.append(i.find("a").get("href"))
    return arr

def video_news():

    site = requests.get("https://dobrewiadomosci.net.pl/category/wideo/")
    content = soup(site.content,'html.parser')

    body = content.find_all("h2",{"class":"entry-title"})
    arr = []
    for i in body:
        arr.append(i.find("a").get("href"))
    return arr   

def health_news():

    site = requests.get("https://dobrewiadomosci.net.pl/category/zdrowie/")
    content = soup(site.content,'html.parser')
    body = content.find_all("h2",{"class":"entry-title"})
    arr = []
    for i in body:
        arr.append(i.find("a").get("href"))
    return arr

