import wolframalpha

app_id = "28KQW5-RVLGPL3KAH"

def inquire(question: str) -> str:
    client = wolframalpha.Client(app_id)
    res = client.query(question)
    return next(res.results).text