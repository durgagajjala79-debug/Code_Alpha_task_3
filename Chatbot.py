"""
CodeAlpha Python Programming Internship
Task 4: Basic Chatbot

A simple rule-based chatbot that responds to predefined user inputs
like greetings, small talk, and farewells.

Key Concepts Used: if-elif, functions, loops, input/output.
"""

import random

# Predefined responses grouped by intent.
# Each intent maps to a list of trigger keywords and a list of possible replies.
RESPONSES = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "good morning", "good evening", "good afternoon"],
        "replies": ["Hi there!", "Hello!", "Hey! Nice to see you."],
    },
    "wellbeing": {
        "keywords": ["how are you", "how're you", "how are you doing"],
        "replies": ["I'm fine, thanks!", "Doing great, thanks for asking!", "I'm just a bunch of code, but I'm doing well!"],
    },
    "name": {
        "keywords": ["what is your name", "what's your name", "who are you"],
        "replies": ["I'm a simple chatbot built for the CodeAlpha internship!", "You can call me CodeAlphaBot."],
    },
    "thanks": {
        "keywords": ["thank you", "thanks", "appreciate it"],
        "replies": ["You're welcome!", "No problem at all!", "Anytime!"],
    },
    "help": {
        "keywords": ["help", "what can you do"],
        "replies": ["I can chat about simple things like greetings, how you're doing, and more. Try saying 'hello'!"],
    },
    "farewell": {
        "keywords": ["bye", "goodbye", "see you", "exit", "quit"],
        "replies": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    },
}

DEFAULT_REPLIES = [
    "I'm not sure I understand. Could you rephrase that?",
    "Sorry, I didn't quite get that.",
    "Hmm, I don't know how to respond to that yet.",
]

FAREWELL_TRIGGERS = RESPONSES["farewell"]["keywords"]


def get_response(user_input):
    """
    Determine the appropriate response based on keyword matching
    in the user's input. Returns the chosen reply string.
    """
    text = user_input.lower().strip()

    for intent, data in RESPONSES.items():
        for keyword in data["keywords"]:
            if keyword in text:
                return random.choice(data["replies"])

    return random.choice(DEFAULT_REPLIES)


def is_farewell(user_input):
    """Check whether the user's input signals they want to end the chat."""
    text = user_input.lower().strip()
    return any(keyword in text for keyword in FAREWELL_TRIGGERS)


def chat():
    print("=" * 40)
    print("CodeAlphaBot: Hello! Type 'bye' to exit anytime.")
    print("=" * 40)

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("CodeAlphaBot: Say something!")
            continue

        response = get_response(user_input)
        print(f"CodeAlphaBot: {response}")

        if is_farewell(user_input):
            break


def main():
    chat()


if __name__ == "__main__":
    main()
