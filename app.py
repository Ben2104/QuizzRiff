from flask import Flask, render_template, request
from inquirer import inquire
import questions
import random

app = Flask(__name__)

global score
score = 0
global quiz
quiz = questions.random_question()

@app.route("/", methods = ["GET", "POST"])
def quizs():
    global score
    global quiz
    if request.method == "POST":
        pre_correct = quiz[1]
        submit_button_value = request.form["answers"]
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

if __name__ == "__main__":
    app.run()
