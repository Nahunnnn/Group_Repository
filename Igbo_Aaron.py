# Aaron_Igbo.py

igbo_dict = {
    "food": "Nri",
    "water": "Mmiri",
    "house": "Ụlọ",
    "person": "Mmadu",
    "child": "Nwa",
    "mother": "Nne",
    "father": "Nna",
    "king": "Eze",
    "work": "Ọrụ",
    "hand": "Aka",
    "ear": "Ntị",
    "eye": "Anya",
    "sun": "Anyānwụ",
    "world": "Ụwa",
    "time": "Oge",
    "year": "Afọ",
    "happiness": "Ọṅụ",
    "fire": "Ọkụ",
    "stone": "Nkume",
    "soup": "Ofe",
}

def translate(word):
    return igbo_dict.get(word.lower(), "Word not found in Igbo dictionary")
while True:
    word = input("Enter an English word (or type 'exit' to quit): ").strip()
    if word.lower() == "exit":
        break
    print(translate(word))