# -- coding: utf-8 --
#hello.py
from approach_to_news import ApproachToNews
from collector import Collector

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

# String 타입의 username 파라메터
# http://localhost:5000/user/사용자명
@app.route('/query/<queryname>')
def get_query(queryname):
	# show the user profile for that user
	s_date = '2020.05.01'
	e_date = '2020.05.20'
	s_from = s_date.replace(".","")
	e_to = e_date.replace(".","")
	page = 1
	query = queryname
	p1=Collector(query,s_date,e_date,s_from,e_to,page)
	p1.saver()

	r = open('new_connection.txt','r')
	return r.read()

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return 'Post %d' % post_id

@app.route('/circle/<float:pi>')
def show_pi(pi):
	return 'PI %f' % pi

@app.route('/path/<path:path>')
def show_path(path):
	return 'path %s' % path


if __name__ == '__main__':
    app.run()