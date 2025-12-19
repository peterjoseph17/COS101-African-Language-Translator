# COS 101 Group Project
# Simple English to Nigerian Language Translator

yoruba = {
    "water": "omi",
    "food": "ounje",
    "house": "ile",
    "school": "ile-iwe",
    "book": "iwe",
    "sun": "oorun",
    "moon": "osupa",
    "child": "omo",
    "man": "okunrin",
    "woman": "obinrin",
    "road": "ona",
    "market": "oja",
    "car": "oko ayokele",
    "money": "owo",
    "fire": "ina",
    "rain": "ojo",
    "tree": "igi",
    "dog": "aja",
    "cat": "ologbo",
    "friend": "ore"
}

print("Welcome to the translator")
print("1. Yoruba")

choice = input("Choose a language: ")

if choice == "1":
    word = input("Enter an English word: ").lower()
    if word in yoruba:
        print("Translation:", yoruba[word])
    else:
        print("Word not found")
else:
    print("Invalid choice")