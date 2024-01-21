import json
import random

print("\n\nAsk the question\nWrite \"STOP\" to stop the coversation!")

data = {
        "hi" : "Hi there!",

        "hello" : "Hello! Ask me",

        "who are you" : "I am a bot",

        "how are you" : ["I am fine! How are you?","All good. How about you?"],
        
        "i am fine" : "That's great!",
        
        "tell me about yourself" : "I am a Chat-bot answering few basic questions.",
        
        "tell me about python" : "Python is a programming language developed by Guido Van Rossum, in 1990. It is a robust language and provide several features.",
        
        "tell me a quote" : ["You never know how STRONG you are until being STRONG is the only choice you have.~by BOB MARLEY","The greatest glory in living lies not in never falling, but rising every time we fall ~ by NELSON MANDELA"],
        
        "tell me a fact" : ["99 percent of our solar system's mass is the sun","-40 °C is equal to -40 °F."],

        "tell me value of pi" : 3.14159265359,

        "tell me value of 22/7" : 3.14159265359,
        
        "suggest one programming language for begnniers" : ["Python","Java","C","C++","C#"],
        
        "difference between git and github" : "Git is a version control system that lets you manage and keep track of your source code history. GitHub is a cloud-based hosting service that lets you manage Git repositories.",
        
        "what is open source" : "Open source is source code that is made freely available for possible modification and redistribution. Products include permission to use the source code,design documents, or content of the product.",
        
        "who is the father of computer" : "Charles Babbage",
        
        "what is AI" : "Artificial intelligence (AI) is the simulation of human intelligence processes by machines, especially computer systems.",
        
        "what is Machine Learning" : "Machine learning is a field of study in artificial intelligence concerned with the development and study of statistical algorithms that can learn from data and generalize to unseen data, and thus perform tasks without explicit instructions.",
        
        "what is algorithm" : "an algorithm is a finite sequence of rigorous instructions, typically used to solve a class of specific problems or to perform a computation. Algorithms are used as specifications for performing calculations and data processing.",
        
        "tell me a fact about math" : "From 0 to 1000, the only number that has the letter “a” in it is one thousand.",

        "smallest moon in the solar system" : "Deimos",

        "which planet is called the morning/evening star" : "Venus",

        "which planets has the shortest revolution period" : "Mercury",

        "what percentage of plastic do we recycle globally" : 9,

        "food waste contributes what percentage of the world's greenhouse gas emissions" : 11,

        "what is the axial tilt of the Earth" : "23.5 Degrees",

        "in which decade with the first transatlantic radio broadcast occur" : 1900,

        "the average power (in watts) used by a 20 to 25 inch home color television is" : "25 to 60 Watts",

        "how many minutes of music can a CD holds" : 74,

        "a computer program that translates a high-level language into machine language is called" : "Complier",

        "crtl + A is used for" : "selecting all text in a document or webpage",

        "what is the name of the second-largest cryptocurrency by market capitalization" : "Ethereum",

        "which computer scientist is known as the father of the World Wide Web" : "Tim Berners-Lee",
        
        "tell another fact" : ["Eleven plus two” is an anagram of twelve plus one which is pretty fitting as the answer to both equations is 13. Also, there are 13 letters in both “eleven plus two” and twelve plus one.","The addition of numbers on the opposite side of dice always equal seven."]

        "thanks" : "You're Welcome!"
}


json_string = json.dumps(data)

data = json.loads(json_string)

while True:
        
    ask = input("User : ")
    if(ask=="0" or ask=="bye" or ask == "end" or ask =="false" or ask=="stop" or ask=="STOP" or ask =="Stop"):
        print("Thanks!")
        break
            
    #special_symbol = ['`','~','!','@','#','$','%','^','&','*','(',')','{','}','[',']','.','/','?','+','-','<','>',',']
    special_symbol = str.maketrans("i", "h", "@#.~`!$%^&*(){}[]:<>?/+-,")
    ask = ask.translate(special_symbol)
    ask = ask.lower()
    #print(ask)

    if(ask not in data):
        print("Sorry I can't answer")
    if("fact" in ask or "quote" in ask or "programming language" in ask):
        print("Bot : ",end=random.choice(data[ask]))
    else:
        print((data[ask]))
            
    print("\n")

    



