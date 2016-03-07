from flask import Flask 
from flask import render_template 

app = Flask("MyQuiz")

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/quiz")
def quiz():
	return render_template("quiz.html")

@app.route("/results")
def results():
	return render_template("results.html")

app.run(
	debug=True)

