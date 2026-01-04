import json
import random
import nltk
from nltk.tokenize import word_tokenize

# Ensure punkt exists (Render-safe)
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

# Load intents
with open("intents.json") as file:
    intents = json.load(file)

def get_response(user_input):
    if not user_input:
        return "Please type something."

    user_input = user_input.lower()
    tokens = word_tokenize(user_input)

    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            pattern_tokens = word_tokenize(pattern.lower())
            if any(word in tokens for word in pattern_tokens):
                return random.choice(intent["responses"])

    return "Sorry, I didn't understand that."
