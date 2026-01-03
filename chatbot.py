import json
import random
import nltk
nltk.download('punkt', quiet=True)
from nltk.tokenize import word_tokenize

# Load intents
with open("intents.json") as file:
    intents = json.load(file)

def get_response(user_input):
    user_input = user_input.lower()
    tokens = word_tokenize(user_input)

    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            pattern_tokens = word_tokenize(pattern.lower())

            # Check if any word matches
            if any(word in tokens for word in pattern_tokens):
                return random.choice(intent["responses"])

    return "Sorry, I didn't understand that. Please try again."
