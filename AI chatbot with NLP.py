import nltk
from nltk.stem import WordNetLemmatizer
import numpy as np
import random
import os

# Download required data
nltk.download('punkt', halt_on_error=True)
nltk.download('wordnet', halt_on_error=True)

# Manually add data path (optional but safe)
nltk.data.path.append(os.path.expanduser('~/AppData/Roaming/nltk_data'))

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Sample intents and responses
intents = {
    "greetings": {
        "patterns": ["hello", "hi", "hey", "good morning", "good evening"],
        "responses": ["Hello!", "Hi there!", "Hey!", "Nice to meet you!"]
    },
    "goodbye": {
        "patterns": ["bye", "see you", "goodbye", "take care"],
        "responses": ["Goodbye!", "See you soon!", "Take care!"]
    },
    "thanks": {
        "patterns": ["thanks", "thank you", "much appreciated"],
        "responses": ["You're welcome!", "Anytime!", "No problem!"]
    },
    "identity": {
        "patterns": ["who are you", "what are you"],
        "responses": ["I'm a simple AI chatbot created for your internship 😊"]
    },
    "default": {
        "responses": ["Sorry, I didn't understand that.", "Can you rephrase?"]
    }
}

# Function to preprocess input
def preprocess(sentence):
    words = nltk.word_tokenize(sentence.lower())  # no language param
    return [lemmatizer.lemmatize(word) for word in words]

# Function to match user input with intent
def get_response(user_input):
    words = preprocess(user_input)
    for intent, intent_data in intents.items():
        for pattern in intent_data.get("patterns", []):
            pattern_words = preprocess(pattern)
            if any(word in words for word in pattern_words):
                return random.choice(intent_data["responses"])
    return random.choice(intents["default"]["responses"])

# Main chatbot loop
print("🤖 Chatbot is ready! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Goodbye! 👋")
        break
    response = get_response(user_input)
    print("Bot:", response)