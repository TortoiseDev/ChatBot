import difflib
# This is a prototype function to determine the values for incomming messages
# The closer the message is to the input the more it will affect the values
# This will require a tuple of dict and percentage of similarity

def calc(a,b,c)-> None:
    print(((a*60/100) + (b*45/100) + (c*80/100))/((60/100 + 45/100 + 80/100)))

def getValues(prompt : str, messages : list) -> dict:
    pass    


calc(10,10,10)