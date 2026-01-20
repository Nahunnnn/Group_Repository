import streamlit as st


st.title("edo Dictionary")

languages = {
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
    "soup": "Ẹkhọ", }


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







       

