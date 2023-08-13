import json
import random
from ngram import NGram

def Train() -> None:
    while True:
        jsonFile = open("Data/Data.json","r")
        data : dict = json.load(jsonFile)
        val_CONFIDENCE : int = 0
        val_CONTEXT : int = 0

        msg_USER_INPUT : str= input("Enter a question: ")
        answers : dict = {}
        i : int = 0
        while True:
            msg_BOT_ANSWER : str= input("Enter its answer(s): ")
            if "!!end" in msg_BOT_ANSWER:
                break
            answers.update({f"Answer{i}" : msg_BOT_ANSWER})
            i+=1

        if "!!end" in msg_USER_INPUT:
            return
        print("Enter context and confidence:")
        val_CONFIDENCE = int(input("Confidence: "))
        val_CONTEXT = int(input("Context: "))
        messRate: dict= {
            "Question": msg_USER_INPUT,
            "Answers":answers,
            "Confidence":val_CONFIDENCE/10,
            "Context" : val_CONTEXT
        }
        data["messages"].append(messRate)
        with open("Data/Data.json","w") as f:
            json.dump(data,f,indent=4)
        print("Message Written!")    

def TrainFromDataSet()->None:
    jsonFile = open("Data/Data.json","r")
    trainingFile = open("Data/trainingData.json","r")
    data : dict = json.load(jsonFile)
    trainingData : list = json.load(trainingFile)["Messages"]
    val_CONFIDENCE : int = 0
    val_CONTEXT : int = 0
    index = int(open("Data/dataIndex.txt","r").read())
    for i in range(index,len(trainingData)):
        print(trainingData[i]["Question"])
        print(trainingData[i]["Answer"])
        print("Enter context and confidence:")
        val_CONFIDENCE = int(input("Confidence: "))
        val_CONTEXT = int(input("Context: "))
        messRate: dict= {
            "Question": trainingData[i]["Question"],
            "Answers":trainingData[i]["Answer"],
            "Confidence":val_CONFIDENCE/10,
            "Context" : val_CONTEXT
        }
        data["messages"].append(messRate)
        with open("Data/Data.json","w") as f:
            json.dump(data,f,indent=4)
        with open("Data/dataIndex.txt","w") as f:
            f.write(str(int(i+1)))
        print("Message Written!")    

def getData() -> any:
    pass       

def selfAction(verb : str,object: str ) -> str:
    pass

def subjectAction(subject : str, verb : str, object :str) -> str:
    pass

def removeCommonWords(message : str) -> str:
    commonWords : set = {"an","a","i","he","she","they","it","them","his","her","them","its",'hers','and','but','were','am','is','are','must','can','in','was','were',"i'm","i've","it's","he's","she's"}
    allWords : list = message.split(' ')
    filteredList : list = [word for word in allWords if word.lower() not in commonWords] 
    joinedText =  ' '.join(filteredList)
    joinedText = joinedText.replace("?","")
    joinedText = joinedText.replace(",","")
    joinedText = joinedText.replace(".","")
    return joinedText

def merge_messages():
    with open("Data/Data.json", 'r') as f:
        data = json.load(f)

    messages = data.get('messages', [])
    merged_messages = {}

    for message in messages:
        question = message.get('Question')
        answer = message.get('Answers')

        if question in merged_messages:
            if isinstance(answer, str):
                answer_keys = sorted(merged_messages[question]['Answers'].keys())
                new_answer_key = f"Answer{len(answer_keys)}"
                merged_messages[question]['Answers'][new_answer_key] = answer
            elif isinstance(answer, dict):
                merged_messages[question]['Answers'] = answer
        else:
            if isinstance(answer, str):
                message['Answers'] = {"Answer0": answer}
            merged_messages[question] = message

    merged_data = {'messages': list(merged_messages.values())}
    with open("Data/Data.json", 'w') as f:
        json.dump(merged_data,f,indent=4)
def getMatches(text: str, possibilities: list, n:float = float("inf"), cutoff : float= 0.6 ):
    text = removeCommonWords(text)
    ngram3 = NGram(n=2)
    ngram4 = NGram(n=4)
    weightOf2 : float = 0.6
    weightOf4 : float = 0.4
    textGram = set(ngram3.ngrams(text))
    textGram4 = set(ngram4.ngrams(text))
    similarText : dict = {}
    for possiblity in possibilities:
        possibleNgram = set(ngram3.ngrams(possiblity))
        possibleNgram4 = set(ngram4.ngrams(possiblity))
        intersection = textGram.intersection(possibleNgram)
        intersection4 = textGram4.intersection(possibleNgram4)
        similarity = len(intersection) / len(textGram)
        similarity4 = len(intersection4) / len(textGram4)
        finalSim = (weightOf2*similarity) + (weightOf4*similarity4)
        similarText.update({finalSim:possiblity})

    similarities : list = sorted(similarText.keys())
    similarities.reverse()
    results : list = []
    for i in range(0,len(similarities)):
        if i >= n:
            break
        if similarities[i] < cutoff:
            break
        results.append((similarities[i],similarText[similarities[i]]))
    return results 

def createDataSet()->None:
    with open("Data/dialogs.txt","r") as f:
        text :str = f.read()
        textLines :list = text.split("\n")
    jsonFile = open("Data/trainingData.json","r")
    jsonData = json.load(jsonFile)
    for pair in textLines:
        lines : list = pair.split("\t")
        if len(lines) == 2:
            jsonData["Messages"].append({"Question":lines[0],"Answer":lines[1]})

    with open("Data/trainingData.json","w") as f:
        json.dump(jsonData,f,indent=4)
    print("Done")
    
def membership(message : str) -> float:
    with open("Data/Data.json" ,"r") as f:
        data = json.load(f)
    questions : dict = {}
    for prompt in data["messages"]:
        questions.update({prompt["Question"]:{"Confidence":prompt["Confidence"],"Context":prompt["Context"]}})
    matches : list  = getMatches(message,questions.keys(),cutoff=0.0)
    if len(matches) == 0:
        return -1
    memebershipDict : dict = {}
    for similarity,question in matches:
        memebershipDict.update({similarity*questions[question]["Confidence"]:question})
    bestList : list = list(memebershipDict.keys())
    bestList = sorted(bestList)
    bestList.reverse()
    cluster = questions[memebershipDict[bestList[0]]]["Context"]
    print(f"Belongs to cluster {cluster} with membership {bestList[0]}")
    return cluster

def getBestAnswer(userMessage : str) -> str:
    messageContext : float = membership(userMessage)
    if messageContext == -1:
        return "Sorry, I didn't quite understand that"
    with open("Data/Data.json",'r') as f:
        trainedData : list = json.load(f)["messages"]
    messagesInthisContext : dict = {}
    for message in  trainedData:
        if message["Context"] == messageContext:
            messagesInthisContext.update({message['Question'].lower():message})
    closestInThisContext : list = getMatches(userMessage,messagesInthisContext.keys(),cutoff=0.5)
    if len(closestInThisContext) == 0:
        return "Sorry, I didn't quite understand that"
    bestMessage : str = closestInThisContext[0][1]
    if type(messagesInthisContext[bestMessage]['Answers']) == dict:
        return random.choice(list(messagesInthisContext[bestMessage]["Answers"].values()))
    
    return messagesInthisContext[bestMessage]["Answers"]
def selfTrain()-> None:
    with open("Data/trainingData.json","r") as f:
        trainingData : list = json.load(f)["Messages"]
    with open("Data/Data.json","r") as f:
        Data : list = json.load(f)
    for message in trainingData:
        messData : dict = {}
        context = membership(message["Question"])
        messagesInthisContext : dict = {}
        for message in  Data["messages"]:
            if message["Context"] == context:
                messagesInthisContext.update({message['Question'].lower():message})
        closestInThisContext : list = getMatches(message["Question"],messagesInthisContext.keys(),cutoff=0.0)
        messData.update({"Question" : message["Question"]})
        messData.update({"Answers" : message["Answers"]})
        messData.update({"Context":context})
        confidence = closestInThisContext[0][0]*messagesInthisContext[closestInThisContext[0][1]]["Confidence"]
        messData.update({"Confidence":confidence})
        Data["messages"].append(messData)
        with open('Data/Data.json',"w") as f:
            json.dump(Data,f,indent=4)
        
MODE : str = input("'Train' the chat or Have a 'fun' chat? \n")

if MODE.lower() == "train":
    print(membership("Hi how are you"))
    # print("Training Mode on")
    # selfTrain()
    merge_messages()
    # trainMode = input("(Train) or Train from (Dataset)")
    # if trainMode.lower() == "dataset":
    #     TrainFromDataSet()
    # else:
    #     Train()
elif MODE == "fun":
    while True:
        print(getBestAnswer(input("Enter message: ")))
