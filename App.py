import json
from math import sqrt 
import difflib

def Train() -> None:
    while True:
        jsonFile = open("Data/Data.json","r")
        data : dict = json.load(jsonFile)
        val_FRIENDLY : int = 0
        val_VULGAR : int = 0
        val_POSITIVE : int = 0
        val_NEGATIVE : int = 0
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
        print("Rate the message from Friendly, Vulgar, Positive, Negative:")
        val_FRIENDLY = int(input("Friendly: "))
        val_VULGAR = int(input("Vulgar: "))
        val_POSITIVE = int(input("Positive: "))
        val_NEGATIVE = int(input("Negative: "))
        val_CONTEXT = int(input("Context: "))
        messRate: dict= {
            "Question":msg_USER_INPUT,
            "Answers":answers,
            "Friendly":val_FRIENDLY,
            "Hateful":val_VULGAR,
            "Positive":val_POSITIVE,
            "Negative":val_NEGATIVE,
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
    val_FRIENDLY : int = 0
    val_VULGAR : int = 0
    val_POSITIVE : int = 0
    val_NEGATIVE : int = 0
    val_CONTEXT : int = 0
    index = int(open("Data/dataIndex.txt","r").read())
    for i in range(index,len(trainingData)):
        print(trainingData[i]["Question"])
        print("Rate the message from Friendly, Vulgar, Positive, Negative:")
        val_FRIENDLY = int(input("Friendly: "))
        val_VULGAR = int(input("Vulgar: "))
        val_POSITIVE = int(input("Positive: "))
        val_NEGATIVE = int(input("Negative: "))
        val_CONTEXT = int(input("Context: "))
        messRate: dict= {
            "Question": trainingData[i]["Question"],
            "Answers":trainingData[i]["Answer"],
            "Friendly":val_FRIENDLY/10,
            "Hateful":val_VULGAR/10,
            "Positive":val_POSITIVE/10,
            "Negative":val_NEGATIVE/10,
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

def getAttributes(message : str) -> dict:
    with open("Data/Data.json" ,"r") as f:
        data : list = json.load(f)["messages"]
        prompts : dict = {}
        for promptData in data:
            prompt : str = promptData["Question"]
            promptDict : dict = {
                "Friendly":promptData['Friendly'],
                "Hateful":promptData['Hateful'],
                "Positive":promptData['Positive'],
                "Negative":promptData['Negative'],
                "Context" : promptData['Context']
            }
            prompts.update({prompt:promptDict})
    matches : list = difflib.get_close_matches(message,prompts.keys(),n=int(len(data)*1/2.9),cutoff=0.5)
    matchesSim : dict = {}
    for match in matches:
        similarity = difflib.SequenceMatcher(None,message,match).ratio()
        matchesSim.update({match:similarity})

    def getValues(prompts:dict,matchesSim : dict) -> dict:
        totalDenum : float = 0
        friendlyTotal : float = 0
        hatefulTotal : float = 0
        positiveTotal : float = 0
        negativeTotal : float = 0
        contextTotal : float = 0
        for message,sim in matchesSim.items():
            friendlyTotal += prompts[message]["Friendly"]*sim
            hatefulTotal += prompts[message]["Hateful"]*sim
            positiveTotal += prompts[message]["Positive"]*sim
            negativeTotal += prompts[message]["Negative"]*sim
            contextTotal += prompts[message]["Context"]*sim
            totalDenum += sim
        return{
            "Friendly":friendlyTotal/totalDenum,
            "Hateful":hatefulTotal/totalDenum,
            "Positive":positiveTotal/totalDenum,
            "Negative":negativeTotal/totalDenum,
            "Context": contextTotal/totalDenum 
        }
    return getValues(prompts,matchesSim)
        

def membership(messageValues : dict) -> float:
    trainedDataFile = open("Data/Data.json","r")
    distances : dict = {}
    for cluster in json.load(trainedDataFile)["messages"]:
        distance : float= sqrt((cluster["Friendly"]-messageValues["Friendly"])**2 +(cluster["Hateful"]-messageValues["Hateful"])**2+(cluster["Positive"]-messageValues["Positive"])**2+(cluster["Negative"]-messageValues["Negative"])**2+(cluster["Context"]-messageValues["Context"])**2)
        distances.update({distance : cluster["Context"]})
    distancesSorted : list = sorted(distances.keys())
    totalItems : int = len(distances)
    k : int = int(totalItems*1/3)
    leastDistances : list = []
    totalDistance : float= 0
    for i in range(0,len(distancesSorted)):
        if i < k:
            leastDistances.append(distancesSorted[i])
        totalDistance += distancesSorted[i]

    def getMostRepeatedCluster(leastDistances : list, distancesAndClusters : dict) -> float:
        clustersAndRepetion : dict = {}
        for distance in leastDistances:
            cluster = distancesAndClusters.get(distance)
            if cluster not in clustersAndRepetion:
                clustersAndRepetion.update({cluster:1})
            else:
                num : int = clustersAndRepetion.get(cluster) + 1
                clustersAndRepetion.update({cluster: num})
        mostReapeated : float = 0
        mostCluster : float = 0
        for cluster,rep in clustersAndRepetion.items():
            if rep > mostReapeated:
                mostReapeated = rep
                mostCluster = cluster
        return mostCluster
    
    cluster = getMostRepeatedCluster(leastDistances,distances)
    thisClusterDistance : int = 0
    for distance,c in distances.items():
        if c == cluster:
            thisClusterDistance += distance

    membership = 1-(thisClusterDistance/totalDistance)
    print(f"Belongs to cluster {cluster} by membership of {membership}")
    return cluster

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
    

MODE : str = input("'Train' the chat or Have a 'fun' chat? \n")

if MODE == "Train":
    print("Training Mode on")
    TrainFromDataSet()

elif MODE == "fun":
    print("Chat mode selected")
    testData = {
        
            "Question": 0,
            "Answers":0,
            "Friendly":0.7,
            "Hateful":0.0,
            "Positive":0.7,
            "Negative":0.0,
            "Context" : 2
        
    }
    # membership(testData)
    print(getAttributes("Hiii, how are you"))