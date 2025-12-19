# Hausa_Nanret.py

hausa_dict = {
    "food": "abinci",
    "water": "ruwa",
    "house": "gida",
    "person": "mutum",
    "child": "yaro",
    "mother": "uwa",
    "father": "uba",
    "king": "sarki",
    "work": "aiki",
    "hand": "hannu",
    "ear": "kunne",
    "eye": "ido",
    "sun": "rana",
    "world": "duniya",
    "time": "lokaci",
    "year": "shekara",
    "happiness": "farin ciki",
    "fire": "wuta",
    "stone": "dutse",
    "soup": "miya"
}

def translate(word):
    return hausa_dict.get(word.lower(), "Word not found in Hausa dictionary")
