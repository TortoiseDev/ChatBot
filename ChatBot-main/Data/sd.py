import json


# This is a prototype function to determine the values for incomming messages
# The closer the message is to the input the more it will affect the values
# This will require a tuple of dict and percentage of similarity

def calc(a, b, c) -> None:
    print(((a * 60 / 100) + (b * 45 / 100) + (c * 80 / 100)) / ((60 / 100 + 45 / 100 + 80 / 100)))


def getValues(prompt: str, messages: list) -> dict:
    pass


def replace() -> None:
    with open("Data/Data.json", "r") as f:
        data = json.load(f)
    finalData: list = []
    for d in data["messages"]:
        question = d["Question"]
        answers = d["Answers"]
        context = d["Context"]
        d.clear()
        d.update({"Question": question})
        d.update({"Answers": answers})
        d.update({"Context": context})
        d.update({"Confidence": 1})
        finalData.append(d)
        with open("Data/Data.json", "w") as f:
            data = json.dump({"messages": finalData}, f, indent=4)


replace()
# calc(10,10,10)
