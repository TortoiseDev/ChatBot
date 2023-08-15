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
            "Question": "why didn't you go to school yesterday?",
            "Answer": "i stayed home because i wasn't feeling well."
        },
        {
            "Question": "i stayed home because i wasn't feeling well.",
            "Answer": "what was your problem?"
        },
        {
            "Question": "what was your problem?",
            "Answer": "my stomach was bothering me."
        },
        {
            "Question": "my stomach was bothering me.",
            "Answer": "are you feeling any better?"
        },
        {
            "Question": "are you feeling any better?",
            "Answer": "i'm still feeling a little sick."
        },
        {
            "Question": "i'm still feeling a little sick.",
            "Answer": "i'm going to the store, would you like any pepto bismol?"
        },
        {
            "Question": "i'm going to the store, would you like any pepto bismol?",
            "Answer": "that's okay."
        },
        {
            "Question": "that's okay.",
            "Answer": "i hope you feel better."
        },
]

def makeSomeData() -> None:
    with open("Data/Data.json","r") as f :
        dataSet = json.load(f)
    for di in data:
        thisData : dict = {}
        que = di["Question"]
        an = di["Answer"]
        context = 12
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