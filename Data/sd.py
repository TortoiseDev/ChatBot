import json
# This is a prototype function to determine the values for incomming messages
# The closer the message is to the input the more it will affect the values
# This will require a tuple of dict and percentage of similarity

def calc(a,b,c)-> None:
    print(((a*60/100) + (b*45/100) + (c*80/100))/((60/100 + 45/100 + 80/100)))

def getValues(prompt : str, messages : list) -> dict:
    pass    

def replace() -> None:
    with open("Data/Data.json","r") as f:
        data = json.load(f)
    finalData : list = []
    for d in data["messages"]:
        question = d["Question"]
        answers = d["Answers"]
        context = d["Context"]
        d.clear()
        d.update({"Question":question})
        d.update({"Answers":answers})
        d.update({"Context":context})
        d.update({"Confidence":1})
        finalData.append(d)
        with open("Data/Data.json","w") as f:
            data = json.dump({"messages":finalData},f,indent=4)

data: list =  [
{
            "Question": "tell me, what do you enjoy doing in your spare time?",
            "Answer": "i enjoy drawing and painting."
        },
        {
            "Question": "i enjoy drawing and painting.",
            "Answer": "you know how to draw and paint?"
        },
        {
            "Question": "you know how to draw and paint?",
            "Answer": "yes, i do."
        },
        {
            "Question": "yes, i do.",
            "Answer": "when did you learn how to do that?"
        },
        {
            "Question": "when did you learn how to do that?",
            "Answer": "i learned back in high school."
        },
        {
            "Question": "i learned back in high school.",
            "Answer": "oh, so you took an art class?"
        },
        {
            "Question": "oh, so you took an art class?",
            "Answer": "yeah, i loved that class."
        },
        {
            "Question": "yeah, i loved that class.",
            "Answer": "i see that you're pretty talented."
        },
        {
            "Question": "i see that you're pretty talented.",
            "Answer": "thank you very much."
        },
        {
            "Question": "thank you very much.",
            "Answer": "i wish i had a talent like that."
        },
        {
            "Question": "i wish i had a talent like that.",
            "Answer": "i'm sure you have a talent. it's just hidden."
        },
        {
            "Question": "what kinds of things do you like to do?",
            "Answer": "i've always liked to draw and paint."
        },
        {
            "Question": "i've always liked to draw and paint.",
            "Answer": "i didn't know you knew how to draw and paint."
        },
        {
            "Question": "i didn't know you knew how to draw and paint.",
            "Answer": "i do it every once in a while."
        },
        {
            "Question": "i do it every once in a while.",
            "Answer": "how long have you known how to do that?"
        },
        {
            "Question": "how long have you known how to do that?",
            "Answer": "i first learned how to do it in high school."
        },
        {
            "Question": "i first learned how to do it in high school.",
            "Answer": "did you take some sort of art class or something?"
        },
        {
            "Question": "did you take some sort of art class or something?",
            "Answer": "that was my favorite class."
        },
        {
            "Question": "that was my favorite class.",
            "Answer": "you have got to be talented."
        },
        {
            "Question": "you have got to be talented.",
            "Answer": "thanks."
        },
        {
            "Question": "thanks.",
            "Answer": "if only i was talented."
        },
        {
            "Question": "if only i was talented.",
            "Answer": "you have a talent. you just don't know what it is yet."
        },
        {
            "Question": "are there any hobbies you do?",
            "Answer": "when i have time, i sometimes draw and paint."
        },
        {
            "Question": "when i have time, i sometimes draw and paint.",
            "Answer": "oh, you actually do that?"
        },
        {
            "Question": "oh, you actually do that?",
            "Answer": "every so often, i do."
        },
        {
            "Question": "every so often, i do.",
            "Answer": "did you always know how to draw and paint?"
        },
        {
            "Question": "did you always know how to draw and paint?",
            "Answer": "i was taught in high school how to draw and paint."
        },
        {
            "Question": "i was taught in high school how to draw and paint.",
            "Answer": "you had an art class?"
        },
        {
            "Question": "you had an art class?",
            "Answer": "exactly, it was my favorite class."
        },
        {
            "Question": "exactly, it was my favorite class.",
            "Answer": "well, it's good that you're so talented."
        },
        {
            "Question": "well, it's good that you're so talented.",
            "Answer": "i appreciate that."
        },
        {
            "Question": "i appreciate that.",
            "Answer": "talent is a great thing, i wish i had one."
        }
]

def makeSomeData() -> None:
    with open("Data/Data.json","r") as f :
        dataSet = json.load(f)
    for di in data:
        thisData : dict = {}
        que = di["Question"]
        an = di["Answer"]
        context = 100
        confidence = 1
        thisData.update({"Question":que})
        thisData.update({"Answers":an})
        thisData.update({"Context":context})
        thisData.update({"Confidence":confidence})
        dataSet["messages"].append(thisData)
        with open("Data/Data.json","w") as f :
            json.dump(dataSet,f,indent=4)

makeSomeData()
# replace()      
# calc(10,10,10)