from inquirer import inquire
import random
import pycountry

TOTAL = 6

def random_question():

    randomized = random.randint(1, 1000000) % TOTAL
    match randomized:
        case 0:
            return name_president()
        case 1:
            return name_capital()
        case 2:
            return addition_problem()
        case 3:
            return subtraction_problem()
        case 4:
            return division_problem()
        # case 5:
        #     return product_problem()


def name_president() -> list:
    answer = list()

    for answers in range(4):
        random_num = random.randint(1, 46)
        question = f"What is the name of the {random_num} president of the United States?"
        if answers == 0:
            answer.append(question)
        ans = inquire(question).split(" (")
        answer.append(ans[0])
    return answer

ignore = [11,20,36,97,105,136,184,195,212,220]
def name_capital():
    countryList = list(pycountry.countries)
    x = [i for i in range(249) if i not in ignore]
    answers = random.sample(x,4)
    questions = []
    ans = []
    for counter in range(4):
        country = list(pycountry.countries)[answers[counter]].name
        questions.append(f"What is the capital of {country}?")
        ans.append(inquire(questions[counter]).split(","))
    return [questions[0], ans[0][0].lstrip(), ans[1][0].lstrip(), ans[2][0].lstrip(), ans[3][0].lstrip()]

def addition_problem():
    a = random.randint(100, 999)
    b = random.randint(100, 999)
    c = a + b
    question = f"What is the result of {a} + {b} = ?"
    return [question, c, random.randint(c-68, c+25), random.randint(c-28, c+75),random.randint(c-48, c+35)]

def subtraction_problem():
    a = random.randint(100, 999)
    b = random.randint(100, 999)
    c = a - b
    question = f"What is the result of {a} - {b} = ?"
    return [question, c, random.randint(c-68, c+25), random.randint(c-28, c+75),random.randint(c-48, c+35)]

def division_problem():
    a = random.randint(50,999)
    b = random.randint(2,15)
    div = a//b
    r = a%b
    divs = random.sample(range(max(0,div-15),div+15),3)
    rs = [random.randint(0,b-1) for i in range(3)]
    question = f"What is the result of {a} / {b} = ?"
    return [question, f"{div} r {r}", f"{divs[0]} r {rs[0]}", f"{divs[1]} r {rs[1]}", f"{divs[2]} r {rs[2]}"]
    
def product_problem():
    a = random.randint(10, 99)
    b = random.randint(10,99)
    c = a * b
    
