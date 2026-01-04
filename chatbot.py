import json
import random
import nltk
import os
from nltk.tokenize import word_tokenize

# Ensure punkt tokenizer exists
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

# Get absolute path to intents.json (RENDER SAFE)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INTENTS_PATH = os.path.join(BASE_DIR, "intents.json")

with open(INTENTS_PATH, "r") as file:
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
