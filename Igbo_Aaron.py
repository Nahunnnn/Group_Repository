import streamlit as st


st.title("igbo Dictionary")

languages = {
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
