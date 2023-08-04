import nltk
from nltk.chat.util import Chat, reflections

# Define the chatbot's responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name?",
        ["You can call me Chatbot.", "I'm Chatbot, nice to meet you."]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?"]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "No problem."]
    ],
    [
        r"quit",
        ["Bye-bye. Take care!"]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!"]
    ],
    [
        r"what is the weather today?",
        ["I'm sorry, I don't have access to real-time weather information."]
    ],
    [
        r"what is your favorite color?",
        ["I'm a chatbot, I don't have preferences."]
    ],
    [
        r"how old are you?",
        ["I am an AI, so I don't have an age."]
    ],
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Start the conversation
print("Hello! I'm a chatbot. How can I assist you today?")
chatbot.converse()
