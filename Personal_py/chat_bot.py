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
# Add more pairs to the list
pairs.extend([
    [
        r"tell me about yourself",
        ["I am a language model AI created by OpenAI. I'm here to help you with your questions and tasks."]
    ],
    [
        r"what can you do?",
        ["I can provide information, answer questions, tell jokes, and assist you with various tasks."]
    ],
    [
        r"who created you?|who is your creator?",
        ["I was created by OpenAI, a leading artificial intelligence research organization."]
    ],
    [
        r"do you have any siblings?|do you know other chatbots?",
        ["I am aware of other chatbots, but I don't have siblings in the traditional sense."]
    ],
    [
        r"what's your favorite food?",
        ["I don't eat, so I don't have a favorite food."]
    ],
    [
        r"can you learn and improve over time?",
        ["I don't learn or improve like humans do, but I am constantly updated by my creators to provide better responses."]
    ],
    [
        r"who won the last World Cup?|tell me about recent sports events",
        ["I don't have access to real-time data, but you can easily find that information online."]
    ],
    [
        r"what's the meaning of life?",
        ["The meaning of life is a philosophical question that has been debated for centuries. It's up to each individual to find their own meaning."]
    ],
])



# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Start the conversation
print("Hello! I'm a chatbot. How can I assist you today?")
chatbot.converse()
