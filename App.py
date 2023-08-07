import json 

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
        print("Rate the message from Friendly, Vulgar, Loving, Boring, Positive, Negative:")
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


def getData() -> any:
    pass       

def selfAction(verb : str,object: str ) -> str:
    pass

def subjectAction(subject : str, verb : str, object :str) -> str:
    pass

def getAttributes(message : str) -> dict:
    pass


    
MODE : str = input("'Train' the chat or Have a 'fun' chat? \n")

if MODE == "Train":
    print("Training Mode on")
    Train()

elif MODE == "fun":
    print("Chat mode selected")