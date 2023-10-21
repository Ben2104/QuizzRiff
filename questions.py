from inquirer import inquire
import random
import pycountry

TOTAL = 2

def random_question():

    randomized = random.randint(1, 1000000) % TOTAL
    match randomized:
        case 0:
            return name_president()
        case 1:
            return name_capital()


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

def name_capital():
    countryList = list(pycountry.countries)
    print(len(countryList))
    answers = random.sample(range(249),4)
    questions = []
    ans = []
    for counter in range(4):
        country = list(pycountry.countries)[answers[counter]].name
        questions.append(f"What is the capital of {country}?")
        ans.append(inquire(questions[counter]).split(","))
    return [questions[0], ans[0][-2].lstrip(), ans[1][-2].lstrip(), ans[2][-2].lstrip(), ans[3][-2].lstrip()]

"""
def product_problem():
    a = random.randint(10, 99)
    b = random.randint(10,99)
    c = a * b
    
"""