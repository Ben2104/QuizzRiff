from inquirer import inquire
import random
import pycountry

app_id = "28KQW5-RVLGPL3KAH"

def name_president() -> list:
    question = f"What was the name of the {random.randint(1, 46)} president of the united states?"
    ans = inquire(app_id, question).split(" (")
    return [question, ans[0]]

def name_capital():
    country = list(pycountry.countries)[random.randint(0,192)].name
    question = f"What is the capital of {country}?"
    ans = inquire(app_id, question).split(",")
    return [question, ans[0]]