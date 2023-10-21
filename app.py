from flask import Flask, render_template, request, redirect
from multiprocessing import Process, Value, Array
import questions
import random
import sqlite3

app = Flask(__name__)

global score
score = 0
question_num = 1
global quiz
quiz = []
global logged
logged = False

@app.route("/", methods = ["GET", "POST"])
def quizs():
    global score
    global quiz
    global logged
    global question_num
    #if logged == False:
    #    return redirect(url_for("/loggin"))
    if request.method == "POST":
        question_num += 1
        pre_correct = quiz[1]
        submit_button_value = request.form["answers"]
        print(submit_button_value)
        if submit_button_value == pre_correct:
            score += 1
        flines = []
        while len(flines) < question_num:
            with open("preloaded.txt",'r') as f:
                flines = f.readlines()
        print(flines[question_num-1])
        quiz = flines[question_num-1].split(",")
        order = random.sample(range(1,5),4)
        return render_template("quiz.html", question=quiz[0],
                               answer1=quiz[order[0]],
                               answer2=quiz[order[1]],
                               answer3=quiz[order[2]],
                               answer4=quiz[order[3]],
                               score=score,
                               correct_answer=pre_correct)
    elif request.method == "GET":
        flines = []
        while len(flines) < question_num:
            with open("preloaded.txt",'r') as f:
                flines = f.readlines()
        quiz = flines[question_num-1].split(",")
        order = random.sample(range(1,5),4)
        return render_template("quiz.html", question=quiz[0], 
                               answer1=quiz[order[0]],
                               answer2=quiz[order[1]],
                               answer3=quiz[order[2]],
                               answer4=quiz[order[3]])

def preload():
    print("preloading")
    numqs = 10
    quizfull = []
    for i in range(numqs):
        q = questions.random_question()
        print(q)
        with open("preloaded.txt", 'a') as f:
            f.write(f"{','.join(q)}\n")


@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    open('preloaded.txt', 'w').close()
    p = Process(target=preload)
    p.start()
    print("after p")
    app.run()
