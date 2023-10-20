import wolframalpha

def inquire(key: str, question: str) -> str:
    client = wolframalpha.Client(key)
    res = client.query(question)
    return next(res.results).text