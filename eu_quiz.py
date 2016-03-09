#Code First Girls lesson 3 on 11 Feb 16 and lesson 4 on 19 Feb 16
import requests
from flask import Flask
from flask import render_template
from flask import request

app = Flask("My App")

@app.route("/")
#the '/' just means the stem i.e. the home page
#the 'app' is just the variable name from above

def eu_quiz():
	return render_template("index.html")
#Flask automatically looks for html templates in a folder called 'templates'. 
#Make sure you have a folder called 'templates'

@app.route("/take-quiz", methods=['POST'])
def quiz_data_collection():
	form_data = request.form
	quiz_results1 = int(form_data['Q1'])
	quiz_results2 = int(form_data['Q2'])
	return u"Your answer is {}".format(quiz_results1 + quiz_results2)

'''def quiz_q1():
	return int(form_data['Q1'])

def quiz_q2():
	return int(form_data['Q2'])'''


#'debug = True' allows it to update itself without you having to re-run it in the terminal/shell
#port=xxxx changes the port so that you would now find the page at: http://127.0.0.1:3672/ <-- for example.
#app.run() needs to go after all the functions, otherwise the functions will not be run!
app.run(
	debug=True, port=3672)