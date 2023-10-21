from flask import Flask, render_template, request
from flask import make_response
import questions
import random

app = Flask(__name__)

def next_question(func):
    quiz = func()
    order = random.sample(range(1,5),4)
    return render_template("index.html", question=quiz[0], 
                           answer1=quiz[order[0]],
                           answer2=quiz[order[1]],
                           answer3=quiz[order[2]],
                           answer4=quiz[order[3]])

@app.route('/login', methods=['GET', 'POST'])
def login():
   print("abababljkda;slifdjoasefijd")
   message = None
   if request.method == 'POST':
        datafromjs = request.form['param']
        print(datafromjs)
        #result = next_question(questions.name_president)
        result = "python response"
        resp = make_response('{"response": '+result+'}')
        resp.headers['Content-Type'] = "application/json"
        return resp
        return render_template('login.html', message='')

if __name__ == "__main__":
    app.run(debug=True)