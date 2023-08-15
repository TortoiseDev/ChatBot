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
            "Question": "it was nice talking to you.",
            "Answer": "why are you trying to rush me off the phone?"
        },
        {
            "Question": "why are you trying to rush me off the phone?",
            "Answer": "i really have to go."
        },
        {
            "Question": "i really have to go.",
            "Answer": "why? i still wanted to talk to you."
        },
        {
            "Question": "why? i still wanted to talk to you.",
            "Answer": "i have things to do."
        },
        {
            "Question": "i have things to do.",
            "Answer": "like what?"
        },
        {
            "Question": "like what?",
            "Answer": "don't be nosey."
        },
        {
            "Question": "don't be nosey.",
            "Answer": "i'm not. i just want to know."
        },
        {
            "Question": "i'm not. i just want to know.",
            "Answer": "well, it's really none of your business."
        },
        {
            "Question": "well, it's really none of your business.",
            "Answer": "that's harsh."
        },
        {
            "Question": "that's harsh.",
            "Answer": "i'm sorry, but i have to go."
        },
        {
            "Question": "i'm sorry, but i have to go.",
            "Answer": "fine."
        },
        {
            "Question": "i've enjoyed conversing with you.",
            "Answer": "is there a reason why you're trying to get off the phone so fast?"
        },
        {
            "Question": "is there a reason why you're trying to get off the phone so fast?",
            "Answer": "i've got to go."
        },
        {
            "Question": "i've got to go.",
            "Answer": "i wasn't done talking to you."
        },
        {
            "Question": "i wasn't done talking to you.",
            "Answer": "i have to do some things, and besides, it's not polite to be nosey."
        },
        {
            "Question": "i have to do some things, and besides, it's not polite to be nosey.",
            "Answer": "i'm not being nosey. i'm just asking."
        },
        {
            "Question": "i'm not being nosey. i'm just asking.",
            "Answer": "i really don't think it's any of your business."
        },
        {
            "Question": "i really don't think it's any of your business.",
            "Answer": "that's not nice."
        },
        {
            "Question": "that's not nice.",
            "Answer": "i apologize, but i'm getting off the phone now."
        },
        {
            "Question": "i apologize, but i'm getting off the phone now.",
            "Answer": "okay."
        },
        {
            "Question": "i'll talk to you later.",
            "Answer": "what's the rush?"
        },
        {
            "Question": "what's the rush?",
            "Answer": "i have to get off the phone now."
        },
        {
            "Question": "i have to get off the phone now.",
            "Answer": "i'm not ready to get off the phone with you."
        },
        {
            "Question": "i'm not ready to get off the phone with you.",
            "Answer": "there are other things i need to take care of."
        },
        {
            "Question": "there are other things i need to take care of.",
            "Answer": "what is it that you need to do? "
        },
        {
            "Question": "what is it that you need to do? ",
            "Answer": "please don't be nosey."
        },
        {
            "Question": "please don't be nosey.",
            "Answer": "i'm not being nosey, it's just a question."
        },
        {
            "Question": "i'm not being nosey, it's just a question.",
            "Answer": "you don't need to worry about that."
        },
        {
            "Question": "you don't need to worry about that.",
            "Answer": "that was mean to say."
        },
        {
            "Question": "that was mean to say.",
            "Answer": "i am very sorry, but i must go."
        },
]

def makeSomeData() -> None:
    with open("Data/Data.json","r") as f :
        dataSet = json.load(f)
    for di in data:
        thisData : dict = {}
        que = di["Question"]
        an = di["Answer"]
        context = 34
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