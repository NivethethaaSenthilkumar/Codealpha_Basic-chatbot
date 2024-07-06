import nltk
from nltk.chat.util import Chat, reflections
nltk.download('punkt')
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by you.",]
    ],
    [
        r"how are you?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "No problem",]
    ],
    [
        r"I am (.*) (good|well|okay|ok)",
        ["Nice to hear that", "Alright, great!",]
    ],
    [
        r"(.*) (age|old) (.*)",
        ["I am a computer program, I don't have an age.",]
    ],
    [
        r"what (.*) want ?",
        ["I want to help you with your queries.",]
    ],
    [
        r"(.*) created ?",
        ["I was created using Python's NLTK library.",]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm in the cloud, I don't have a physical location.",]
    ],
    [
        r"how (.*) weather (.*)",
        ["I can't check the weather, but it's always sunny in the digital world.",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon!",]
    ],
    [
        r"(.*)",
        ["I didn't understand that. Can you rephrase?",]
    ],
]

def chatbot():
    print("Hi, I'm a chatbot created by you. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
