import streamlit as st


st.title("yoruba Dictionary")

languages = {


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

user_word = st.text_input("Enter a word you would like to translate").strip().lower()
if  st.button("Translate"):
    if user_word:
        #check if the word exists in the dictionary
        if user_word in languages:
            translation = languages[user_word]
            st.success(f"**translation:** {translation}")
        else:
            st.warning("sorry,word not in dictionary")
    else:
        st.warning("Please enter a word first")






