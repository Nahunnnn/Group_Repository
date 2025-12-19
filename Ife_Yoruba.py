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

print("Welcome to Yoruba Dictionary, What word would you like to translate to Yoruba? ")
print("type 'exit' to quit")

while True:
    word=input("Enter an English word").lower()
    if word == "exit":
        print("goodbye")
        break

    if word in yoruba_dict:
        print("Yoruba translator:",
              yoruba_dict[word])
    else:
        print("sorry,word not in dictionary")

