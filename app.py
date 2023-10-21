from flask import Flask, render_template
from inquirer import inquire
import questions

app = Flask(__name__)

@app.route('/')
def index():
    quiz = questions.name_president()
    return render_template("index.html", question=quiz[0], 
                           answer1=quiz[1],
                           answer2=quiz[2],
                           answer3=quiz[3],
                           answer4=quiz[4])

if __name__ == "__main__":
    app.run()