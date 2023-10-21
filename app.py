from flask import Flask, render_template, request, redirect, url_for
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
global username
global user_score

global top_users
top_users = list()

conn =  sqlite3.connect("user_data.db", check_same_thread=False)
cursor = conn.cursor()

@app.route("/", methods = ["GET", "POST"])
def quizs():
    global score
    global quiz
    global logged
    global question_num
    global top_users
    
    cursor.execute("SELECT username, score FROM users LIMIT 5")
    top_users = cursor.fetchall()
    top_users = list(reversed(sorted(top_users, key=lambda x:x[1])))
    
    if logged == False:
        return redirect(url_for("login"))
    
    if request.method == "POST":
        # question_num += 1
        pre_correct = quiz[1]
        submit_button_value = request.form["answers"]
        print(submit_button_value)
        if submit_button_value == pre_correct:
            cursor.execute("UPDATE users SET score = ? WHERE username = ?", ((user_score + 1), username))
            conn.commit()
        # flines = []
        # while len(flines) < question_num:
            # with open("preloaded.txt",'r') as f:
                # flines = f.readlines()
        # print(flines[question_num-1])
        # quiz = flines[question_num-1].split(",")
        try:
            quiz = questions.random_question()
        except StopIteration:
            return redirect("/")
        order = random.sample(range(1,5),4)
        return render_template("quiz.html", question=quiz[0],
                               answer1=quiz[order[0]],
                               answer2=quiz[order[1]],
                               answer3=quiz[order[2]],
                               answer4=quiz[order[3]],
                               score=user_score,
                               correct_answer=pre_correct,
                               top_users=top_users)
    elif request.method == "GET":
        # flines = []
        # while len(flines) < question_num:
            # with open("preloaded.txt",'r') as f:
                # flines = f.readlines()
        # quiz = flines[question_num-1].split(",")
        quiz = questions.random_question()
        order = random.sample(range(1,5),4)
        return render_template("quiz.html", question=quiz[0], 
                               answer1=quiz[order[0]],
                               answer2=quiz[order[1]],
                               answer3=quiz[order[2]],
                               answer4=quiz[order[3]],
                               top_users=top_users)

def preload():
    print("preloading")
    numqs = 10
    quizfull = []
    for i in range(numqs):
        q = questions.random_question()
        print(q)
        with open("preloaded.txt", 'a') as f:
            f.write(f"{','.join(q)}\n")


@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        submit_username = request.form["username"]
        submit_password = request.form["password"]
        cursor.execute("SELECT username, password, score FROM users WHERE username = ?", (submit_username,))
        user = cursor.fetchall()
        if len(user) == 1:
            if submit_password == user[0][1]:
                global logged
                logged = True
                global username
                username = submit_username
                global user_score
                user_score = user[0][2]
        else:
            return redirect(url_for("signup"))
        return redirect(url_for("quizs"))


@app.route("/signup", methods = ["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    elif request.method == "POST":
        global logged
        submit_username = request.form["username"].lower()
        submit_password = request.form["password"]
        cursor.execute("SELECT username FROM users WHERE username = ?", (submit_username,))
        user = cursor.fetchall()
        if len(user) == 0:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (submit_username, submit_password))
            conn.commit()
            global username
            username = submit_username
            logged = True
        else:
            return redirect(url_for("login"))
        return redirect(url_for("quizs"))




if __name__ == "__main__":
    # open('preloaded.txt', 'w').close()
    # p = Process(target=preload)
    # p.start()
    # print("after p")
    app.run()

