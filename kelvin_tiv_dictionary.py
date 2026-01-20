#  English to Tiv Translator
tiv_dictionary = {
"helllo":"M sugh",
"goodbye": "kwase",
"thank you": "A vo",
"yes": "Ee",
"no": "Ao",
"water": "minger",
"food": "ishima",
"man": "or",
"woman": "mba",
"child": "wan",
"house": "ya",
"road": "tar",
"sun": "ushar",
"moon": "ikyo",
"fire": "kure",
"love": "hemen",
"friend": "manger",
"school": "kwagh u ishim",
"book": "ityo",
"money": "kpen"
}

print("EINGLIH -> TIV TRANSLATOR")
print("type 'exit' to quit")

while True:
    word=input("Enter an English word").lower()
    if word == "exit":
        print("goodbye")
        break

    if word in tiv_dictionary:
        print("TIV translator:",
              tiv_dictionary[word])
    else:
        print("sorry,word not in dictionary")
