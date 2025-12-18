#Ife_Yoruba.py

yoruba_dict = {
    "Bawo": "How",
    "Ekaaro": "Good Morning",
    "Ejo": "Please",
    "Duro": "Wait",
    "Ope": "Thanks",
    "Ile": "House",
    "Omi": "Water",
    "Onje": "Food",
    "Baba": "Father",
    "Iya": "Mother",
    "Omode": "Child",
    "Aro": "Soap",
    "Oja": "Market",
    "Ona": "Road",
    "Iwa": "Character",
    "Efun": "Forgiveness",
    "Ayo": "Joy",
    "Ibeji": "Twins",
    "Ifa": "Oracle",
    "Odu": "Chapter",
}

def translate(word):
    return yoruba_dict.get(word.lower(), "Word not found in Yoruba Dictionary")