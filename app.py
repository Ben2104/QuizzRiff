from flask import Flask, render_template, request
from inquirer import inquire
import questions

app = Flask(__name__)

global score
score = 0
global quiz
quiz = questions.name_president()

@app.route("/", methods = ["GET", "POST"])
def quizs():
    global score
    global quiz
    if request.method == "POST":
        pre_correct = quiz[1]
        submit_button_value = request.form["answers"]
        if submit_button_value == quiz[1]:
            score += 1
        quiz = questions.name_president()
        return render_template("quiz.html", questions=quiz[0],
                               answer1=quiz[1],
                               answer2=quiz[2],
                               answer3=quiz[3],
                               answer4=quiz[4],
                               score=score,
                               correct_answer=pre_correct)
    elif request.method == "GET":

        return render_template("quiz.html", question=quiz[0], 
                               answer1=quiz[1],
                               answer2=quiz[2],
                               answer3=quiz[3],
                               answer4=quiz[4])

if __name__ == "__main__":
    app.run()
