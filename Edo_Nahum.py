# edo.py

edo_dict = {
        "food": "Ẹghẹn",
        "Water": "Ami",
        "house": "Ẹvbu",
        "person": "Edo",
        "child": "Ọmọ",
        "mother": "Iyẹn",
        "father": "Baba",
        "king": "Oba",
        "work": "Ise",
        "hand": "Ovbẹ",
        "ear": "Oto",
        "eye": "Egho",
        "sun": "Ọwan",
        "world": "Uwa",
        "time": "Ẹghe",
        "year": "Ọghe",
        "happiness": "Uyi",
        "fire": "Ina",
        "stone": "Ẹdo",
        "soup": "Ẹkhọ",}


def translate(word):
    return edo_dict.get(word.lower(), "Word not found in Edo dictionary")


       