#Code First Girls lesson 3 on 11 Feb 16 and lesson 4 on 19 Feb 16
import requests
from flask import Flask
from flask import render_template
from flask import request
import tweepy
import csv
import unicodecsv

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

	result1 = int(form_data['Q1'])
	result2 = int(form_data['Q2'])
	result3 = int(form_data['Q3'])
	result4 = int(form_data['Q4'])
	result5 = int(form_data['Q5'])
	result6 = int(form_data['Q6'])
	result7 = int(form_data['Q7'])
	result8 = int(form_data['Q8'])
	result9 = int(form_data['Q9'])
	result10 = int(form_data['Q10'])

	quiz_results_added = result1 + result2 + result3 + result4 + result5 + result6 + result7 + result8 + result9 + result10

	save_comment(request)

	if quiz_results_added >= 0 and quiz_results_added <= 10:
		return leave()
	elif quiz_results_added >= 11 and quiz_results_added <= 20:
		return maybe_leave()
	elif quiz_results_added >= 21 and quiz_results_added <= 30:
		return maybe_stay()
	else:
		return stay()



def stay():
	return render_template("stay.html")

def maybe_stay():
	return render_template("maybe_stay.html")

def maybe_leave():
	return render_template("maybe_leave.html")

def leave():
	return render_template("leave.html")


def save_comment(request):
    print 'All working!'
       
    Q1 = request.form['Q1']
    Q2 = request.form['Q2']
    Q3 = request.form['Q3']
    Q4 = request.form['Q4']
    Q5 = request.form['Q5']
    Q6 = request.form['Q6']
    Q7 = request.form['Q7']
    Q8 = request.form['Q8']
    Q9 = request.form['Q9']
    Q10 = request.form['Q10']


    fieldnames = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10']

    with open('eu_spreadsheet.csv','a') as inFile:
          
    	writer = csv.DictWriter(inFile, fieldnames=fieldnames)

        writer.writerow({'Q1': Q1, 'Q2': Q2, 'Q3': Q3, 'Q4': Q4, 'Q5': Q5, 'Q6': Q6, 'Q7': Q7, 'Q8': Q8, 'Q9': Q9, 'Q10': Q10})


#return u"Your answer is {}".format(quiz_results1 + quiz_results2)

#def quiz_q1():
#	return int(form_data['Q1'])

#def quiz_q2():
#	return int(form_data['Q2'])

#'debug = True' allows it to update itself without you having to re-run it in the terminal/shell
#port=xxxx changes the port so that you would now find the page at: http://127.0.0.1:3672/ <-- for example.
#app.run() needs to go after all the functions, otherwise the functions will not be run!
app.run(
	debug=True, port=3672)