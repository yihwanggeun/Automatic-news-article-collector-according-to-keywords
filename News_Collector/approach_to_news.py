import requests
from bs4 import BeautifulSoup
import json
import re
import sys
import time, random


class ApproachToNews:
    def __init__(self):
        self.n_url=""

    def get_news(self,n_url): 
        self.n_url = n_url
        news_detail = [] 
        breq = requests.get(self.n_url) 
        bsoup = BeautifulSoup(breq.content, 'html.parser') 
        
       
        title = bsoup.select('h3#articleTitle')[0].text 
        news_detail.append(title) 

        pdate = bsoup.select('.t11')[0].get_text()[:11] 
        news_detail.append(pdate) 

        _text = bsoup.select('#articleBodyContents')[0].get_text().replace('\n', " ") 
        btext = _text.replace("function _flash_removeCallback() {}", "") 
        news_detail.append(btext.strip()) 

        return news_detail
