import json
import random
import os

# Load intents.json safely
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INTENTS_PATH = os.path.join(BASE_DIR, "intents.json")

with open(INTENTS_PATH, "r") as file:
    intents = json.load(file)

def get_response(user_input):
    if not user_input:
        return "Please type something."

    user_input = user_input.lower()

    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if pattern.lower() in user_input:
                return random.choice(intent["responses"])

    return "Sorry, I didn't understand that."
