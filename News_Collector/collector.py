#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
import re
import sys
import time, random
from approach_to_news import ApproachToNews

class Collector:
  def __init__(self,query,s_date,e_date,s_from,e_to,count):
      self.query =  query
      self.s_date = s_date
      self.e_date = e_date
      self.s_from = s_from
      self.e_to = e_to
      self.count = int(count)

  def saver(self):
      f = open("templates/new_connection.html",'w')
      news_client = ApproachToNews()
      page = 1
      f.write('<head>')
      f.write('</head>')
      f.write('<body>')
      f.write('<h1 style="background-color: antiquewhite; font-size:200%"> ')
      f.write('뉴스 수집기')
      f.write('</h1>')
      while page<self.count:
          url = "https://search.naver.com/search.naver?where=news&query="+self.query + "&sort=1&ds=" + self.s_date + "&de=" + self.e_date + "&nso=so%3Ar%2Cp%3Afrom" + self.s_from + "to" + self.e_to + "%2Ca%3A&start=" + str(page) +"&refresh_start=0"
          print(url)
          response = requests.get(url)
          content = response.content
          furl= BeautifulSoup(content,'html.parser')
          for urls in furl.select("._sp_each_url"):   
              if urls["href"].startswith("https://news.naver.com"):
                news_detail = news_client.get_news(urls["href"])
                f.write('<p>')
                f.write(news_detail[1])
                f.write('<br>')
                f.write(news_detail[0])
                f.write('<br>')
                f.write(news_detail[2])
                f.write('</br>')
                f.write('</p>')
                         
              #  f.write("{}\t{}\t{}\n".format(news_detail[1], news_detail[0], news_detail[2]))
          page+=10
          f.write('</body>')       
      f.close()       
                    
      
                        
                
	

