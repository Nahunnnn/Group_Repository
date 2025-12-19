yoruba_dict = {
    "how": "Bawo",
    "good morning": "Ekaaro",
    "please": "Ejo",
    "wait": "Duro",
    "thanks": "Ope",
    "house": "Ile",
    "water": "Omi",
    "food": "Onje",
    "father": "Baba",
    "mother": "Iya",
    "child": "Omode",
    "soap": "Aro",
    "market": "Oja",
    "road": "Ona",
    "character": "Iwa",
    "forgiveness": "Efun",
    "joy": "Ayo",
    "twins": "Ibeji",
    "oracle": "Ifa",
    "chapter": "Odu"
}

word = input("Welcome to Yoruba Dictionary! Please enter a word: ")

word = word.strip().lower()  

if word in yoruba_dict:
    print(f"The meaning in Yoruba is: {yoruba_dict[word]}")
else:
    print("Word not found in Yoruba Dictionary")
