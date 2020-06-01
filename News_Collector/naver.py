#-*- coding:utf-8 -*-
import os
import sys
import urllib.request
from urllib.parse import *
import requests
from bs4 import BeautifulSoup
import json
import re
import sys
import time, random
import pandas as pd

def clean_html(x):
  x = re.sub("\&\w*\;","",x)
  x = re.sub("<.*?>","",x)
  return x
def crawling(News_Name,Page):
  News = News_Name
  display = Page
  headers = ({
  "X-Naver-Client-Id" : "0DsbMBvJDgtTOQ2D9wLM",
  "X-Naver-Client-Secret" : "ImissXdl3I"
  })

  encText = requests.utils.quote(News)
  url = "https://openapi.naver.com/v1/search/news.json?query="+ encText  +"&display=" + str(display) +"&sort=sim"

  response = requests.get(url,headers=headers)
  content = response.content
  rescode = response.status_code
  response.encoding = 'utf-8'
  response_body = response.json()
  df = pd.DataFrame(response_body['items'])

  df['title'] = df['title'].apply(lambda x: clean_html(x))
  df['description'] = df['description'].apply(lambda x: clean_html(x))

  df.to_csv(f'news_search_result_{News}.csv')
  #df['title'].to_csv(f'news_search_result_{News}_title.csv')
  #df['originallink'].to_csv(f'news_search_result_{News}_originallink.csv')
  #df['link'].to_csv(f'news_search_result_{News}_link.csv')
  #df['description'].to_csv(f'news_search_result_{News}_description.csv')
  #df['pubDate'].to_csv(f'news_search_result_{News}_pubDate.csv')





                        
                
	

