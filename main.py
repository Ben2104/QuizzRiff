import questions
from flask import Flask, render_template

def main():
    quiz = questions.name_president()
    #quiz = questions.name_capital()
    print(quiz)
    render_template("index.html",)
    


if __name__ == "__main__":
    main()