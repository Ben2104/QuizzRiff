from flask import Flask, render_template, request, redirect, url_for
import questions
import random
import sqlite3

app = Flask(__name__)


global score
score = 0
global quiz
quiz = questions.random_question()
global logged
logged = False

@app.route("/", methods = ["GET", "POST"])
def quizs():
    global score
    global quiz
    global logged
    if logged == False:
        return redirect(url_for("login"))
    if request.method == "POST":
        pre_correct = quiz[1]
        submit_button_value = request.form["answers"]
        print(submit_button_value)
        if submit_button_value == pre_correct:
            score += 1
        quiz = questions.random_question()
        order = random.sample(range(1,5),4)
        return render_template("quiz.html", question=quiz[0],
                               answer1=quiz[order[0]],
                               answer2=quiz[order[1]],
                               answer3=quiz[order[2]],
                               answer4=quiz[order[3]],
                               score=score,
                               correct_answer=pre_correct)
    elif request.method == "GET":
        order = random.sample(range(1,5),4)
        return render_template("quiz.html", question=quiz[0], 
                               answer1=quiz[order[0]],
                               answer2=quiz[order[1]],
                               answer3=quiz[order[2]],
                               answer4=quiz[order[3]])

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        return redirect(url_for("logging"))

@app.route("/logging", methods = ["GET", "POST"])
def logging():
    global logged
    logged = True
    return redirect(url_for("quizs"))

if __name__ == "__main__":
    app.run()

