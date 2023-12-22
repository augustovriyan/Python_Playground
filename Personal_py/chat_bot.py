import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot responses
pairs = [
    [r"my name is (.*)", ["Hello %1, how are you feeling today?"]],
    [r"hi|hey|hello", ["Hello!", "Hey there!"]],
    [r"what is your name?", ["You can refer to me as Chatbot.", "I'm Chatbot. Nice to meet you!"]],
    [r"how are you\?", ["I'm doing well. How about yourself?"]],
    [r"sorry (.*)", ["No worries.", "It's okay."]],
    [r"quit", ["Goodbye! Take care."]],
    [r"tell me a joke", ["Why don't scientists trust atoms? Because they make up everything!"]],
    [r"what is the weather today?", ["I can't provide real-time weather updates."]],
    [r"what is your favorite color?", ["As a chatbot, I don't have preferences."]],
    [r"how old are you?", ["I'm an AI, so age doesn't apply to me."]],
    [r"tell me about yourself", ["I'm an AI language model developed by OpenAI, designed to assist and answer questions."]],
    [r"what can you do?", ["I can answer questions, provide information, tell jokes, and more."]],
    [r"who created you\?|who is your creator\?", ["I was developed by OpenAI, a renowned AI research organization."]],
    [r"do you have any siblings\?|do you know other chatbots\?", ["I'm aware of other chatbots, but I don't have 'siblings' in the conventional sense."]],
    [r"what's your favorite food?", ["I don't consume food, so I don't have preferences."]],
    [r"can you learn over time\?", ["I don't learn like humans, but I receive updates to enhance my functionality."]],
    [r"who won the last World Cup\?|recent sports events", ["I can't fetch real-time data, but you can search online for the latest updates."]],
    [r"what's the meaning of life\?", ["That's a profound question! The meaning of life varies for each individual."]],
]

# Initialize the chatbot
chatbot = Chat(pairs, reflections)

# Start the conversation
print("Hello! I'm a chatbot here to help. How can I assist you today?")
chatbot.converse()
