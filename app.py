from flask import Flask, render_template, request, redirect
from flask_sock import Sock
import questions
import random
import sqlite3

app = Flask(__name__)
sock = Sock(app)

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
        return redirect(url_for("/loggin"))
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

@app.route("/login")
def login():
    return render_template("login.html")

#@app.route("/logging")

#def Logging():

@sock.route('/echo')
def echo(sock):
    global score
    global quiz
    print("echo")
    pre_correct = quiz[1]
    #submit_button_value = request.form["answers"]
    submit_button_value = sock.receive()
    priint(submit_button_value)
    if submit_button_value == pre_correct:
        score += 1
    quiz = questions.random_question()
    order = random.sample(range(1,5),4)
    return sock.send(question=quiz[0],
                            answer1=quiz[order[0]],
                            answer2=quiz[order[1]],
                            answer3=quiz[order[2]],
                            answer4=quiz[order[3]],
                            score=score,
                            correct_answer=pre_correct)


if __name__ == "__main__":
    app.run()
