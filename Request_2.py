#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
import re
import sys
import time, random

def get_news(n_url): 
    news_detail = [] 
    print(n_url) 
    breq = requests.get(n_url) 
    bsoup = BeautifulSoup(breq.content, 'html.parser') 

    title = bsoup.select('h3#articleTitle')[0].text 
    news_detail.append(title) 


    pdate = bsoup.select('.t11')[0].get_text()[:11] 
    news_detail.append(pdate) 

    _text = bsoup.select('#articleBodyContents')[0].get_text().replace('\n', " ") 
    btext = _text.replace("function _flash_removeCallback() {}", "") 
    news_detail.append(btext.strip()) 

    return news_detail


    

query =  "코로나"
s_date = (input("From : "))
e_date = (input("End : "))
s_from = s_date.replace(".","")
e_to = e_date.replace(".","")
page = 1

while page<100:
    print(page)
    url = "https://search.naver.com/search.naver?where=news&query="+query + "&sort=1&ds=" + s_date + "&de=" + e_date + "&nso=so%3Ar%2Cp%3Afrom" + s_from + "to" + e_to + "%2Ca%3A&start=" + str(page) 

    response = requests.get(url)
    content = response.content
    furl= BeautifulSoup(content,'html.parser')
    for urls in furl.select("._sp_each_url"):   
        if urls["href"].startswith("https://news.naver.com"):
            news_detail = get_news(urls["href"])
            print(len(news_detail))
            print(news_detail[1], news_detail[0], news_detail[2])
        page+=10
           
                    
                    
      
                        
                
	

