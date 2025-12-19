#Ife_Yoruba.py

yoruba_dict = {
    "How": "Bawo",
    "Good Morning": "Ekaaro",
    "Please": "Ejo",
    "Wait": "Duro",
    "Thanks": "Ope",
    "House": "Ile",
    "Water": "Omi",
    "Food": "Onje",
    "Father": "Baba",
    "Mother": "Iya",
    "Child": "Omode",
    "Soap": "Aro",
    "Market": "Oja",
    "Road": "Ona",
    "Character": "Iwa",
    "Forgiveness": "Efun",
    "Joy": "Ayo",
    "Twins": "Ibeji",
    "Oracle": "Ifa",
    "Chapter": "Odu",
}

def translate(word):

    return yoruba_dict.get(word.lower(), "Word not found in Yoruba Dictionary")
