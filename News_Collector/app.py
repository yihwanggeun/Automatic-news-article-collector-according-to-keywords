# -- coding: utf-8 --
import csv
# For reading CSV type files
#import sys
import pandas 
# For refatoring some data from crawling
from collector import Collector
# Crawling using html 
from flask import Flask, render_template, request
# For launching Web Server
from naver import crawling
# Crawling using Naver internal API
app = Flask(__name__)

@app.route('/')
def start():
   return render_template('api.html')
# if you send access to server, Launch api.html

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      crawling(request.form["News_Name"],request.form["Page"])
      #Start Crawling
      with open(f'news_search_result_{request.form["News_Name"]}.csv') as csvfile:
         reader = csv.DictReader(csvfile)
         with open ('templates/result.html','w') as htmlfile:
            htmlfile.write('<head>')
            htmlfile.write('</head>')
            htmlfile.write('<body>')
            htmlfile.write('<h1 style="background-color: antiquewhite; font-size:200%"> ')
            htmlfile.write('뉴스 수집기')
            htmlfile.write('</h1>')
            htmlfile.write('<table>')
            for row in reader:
               htmlfile.write('<tr style="border: #56738c !important;border-width: thick !important; font-size: large; font-family: sans-serif;">')
               for k, v in row.items():
                  if k!='':
                   htmlfile.write('<td>')
                   htmlfile.write(f'{v}')
                   htmlfile.write('</td>')
               htmlfile.write('<tr>')
               htmlfile.write('\n')
            htmlfile.write('</table>')
            htmlfile.write('</body>')
      return render_template('result.html')

@app.route('/query')
def start_query():
   return render_template('using_html.html')
  
@app.route('/query/detail',methods = ['POST', 'GET'])
def get_query():
	# show the user profile for that user
	s_date = request.form["Start_Date"]
	e_date = request.form["End_Date"]
	s_from = s_date.replace(".","")
	e_to = e_date.replace(".","")
	count = request.form["Quantity"]
	query = request.form["News_Name"]
	p1=Collector(query,s_date,e_date,s_from,e_to,count)
	p1.saver()



	return render_template('new_connection.html')

if __name__=='__main__':
	app.run()